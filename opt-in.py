#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# dependencies = ["rich"]
# ///

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path

from rich.console import Console

VERSION = "1.2.0"

console = Console()

AGENT_DIR = Path(__file__).parent / "agent"

FRAMEWORK_FILES = ["README.md", "PROCESS.md", "STYLE.md", "MAP-GUIDANCE.md"]

POINTER_PATTERN = re.compile(r"^@(agent/README\.md|changes/agents?/.*README\.md)\s*$")

VERSION_HEADING_PATTERN = re.compile(r"^##\s+(\d+\.\d+\.\d+)\s*$")


def git_root() -> Path:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        console.print("[bold red]Error:[/bold red] not inside a git repository.")
        sys.exit(1)
    return Path(result.stdout.strip())


def main():
    parser = argparse.ArgumentParser(
        description="Opt a project in to the agent change process."
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {VERSION}")
    parser.parse_args()

    project_root = git_root()
    console.print(f"Setting up agent process in [bold]{project_root}[/bold]\n")

    if AGENT_DIR.resolve() == (project_root / "agent").resolve():
        console.print(
            "[bold red]Error:[/bold red] refusing to run — source and destination resolve to the same path.\n"
            "This script is its own source of truth; running it here would install the agent files on top of themselves."
        )
        sys.exit(1)

    version_name = read_latest_version_from_changelog()
    version_dir = project_root / "changes/agent" / version_name
    new_pointer = f"@changes/agent/{version_name}/README.md\n"

    copy_framework_files(version_dir)
    copy_changelog(project_root)

    pointer_outcome = rewrite_claude_md(project_root, new_pointer)

    create_settings(
        project_root / ".claude" / "settings.local.json",
        excludes=["~/.claude/CLAUDE.md"],
    )

    create_dir(project_root / "changes/open")
    create_dir(project_root / "changes/archive")

    update_gitignore(project_root / ".gitignore")

    warn_if_legacy_layout(project_root, pointer_outcome)

    console.print(
        f"\n[bold green]Done.[/bold green] Installed as [bold]{version_name}[/bold]."
    )
    console.print(
        f"Release notes: [dim]{project_root / 'changes/agent/CHANGELOG.md'}[/dim]"
    )


def read_latest_version_from_changelog() -> str:
    changelog = AGENT_DIR / "CHANGELOG.md"
    if not changelog.exists():
        console.print(
            "[bold red]Error:[/bold red] source CHANGELOG.md not found — cannot determine version."
        )
        sys.exit(1)
    for line in changelog.read_text().splitlines():
        match = VERSION_HEADING_PATTERN.match(line)
        if match:
            return match.group(1)
    console.print(
        "[bold red]Error:[/bold red] no `## X.Y.Z` semver section found in CHANGELOG.md."
    )
    sys.exit(1)


def copy_framework_files(version_dir: Path) -> None:
    for name in FRAMEWORK_FILES:
        copy_asset(AGENT_DIR / name, version_dir / name)

    additional_src = AGENT_DIR / "ADDITIONAL"
    additional_dest = version_dir / "ADDITIONAL"
    if additional_src.is_dir():
        for f in sorted(additional_src.iterdir()):
            if f.is_file():
                copy_asset(f, additional_dest / f.name)


def copy_changelog(project_root: Path) -> None:
    src = AGENT_DIR / "CHANGELOG.md"
    dest = project_root / "changes/agent/CHANGELOG.md"
    if not src.exists():
        report("conflict", dest, "source CHANGELOG.md missing — skipped")
        return
    content = src.read_text()
    already_existed = dest.exists()
    if already_existed and dest.read_text() == content:
        report("already present", dest)
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content)
    report("updated" if already_existed else "created", dest)


def copy_asset(src: Path, dest: Path) -> None:
    content = src.read_text()
    if dest.exists():
        if dest.read_text() == content:
            report("already present", dest)
            return
        dest.write_text(content)
        report("updated", dest)
        return
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(content)
    report("created", dest)


def create_file(path: Path, content: str) -> None:
    if path.exists():
        if path.read_text() == content:
            report("already present", path)
        else:
            report("conflict", path, "exists with different content — left untouched")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)
    report("created", path)


def create_settings(path: Path, excludes: list[str]) -> None:
    desired = {"claudeMdExcludes": excludes}
    if path.exists():
        try:
            existing = json.loads(path.read_text())
        except json.JSONDecodeError:
            report("conflict", path, "could not parse JSON — left untouched")
            return
        if "claudeMdExcludes" in existing:
            if existing["claudeMdExcludes"] == excludes:
                report("already present", path)
            else:
                report("conflict", path, "claudeMdExcludes already set to a different value — left untouched")
            return
        existing["claudeMdExcludes"] = excludes
        path.write_text(json.dumps(existing, indent=2) + "\n")
        report("updated", path)
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(desired, indent=2) + "\n")
    report("created", path)


def create_dir(path: Path) -> None:
    if path.exists():
        report("already present", path)
        return
    path.mkdir(parents=True, exist_ok=True)
    report("created", path)


def update_gitignore(path: Path) -> None:
    entries = ["CLAUDE.md", "changes/agent/"]
    content = path.read_text() if path.exists() else ""
    lines = content.splitlines()
    to_add = [e for e in entries if e not in lines]
    if not to_add:
        report("already present", path)
        return
    separator = "\n" if content and not content.endswith("\n") else ""
    block = "\n".join(to_add)
    with path.open("w") as f:
        f.write(content + separator + block + "\n")
    report("updated", path, f"added: {', '.join(to_add)}")


def rewrite_claude_md(project_root: Path, new_pointer: str) -> str:
    path = project_root / "CLAUDE.md"
    if not path.exists():
        path.write_text(new_pointer)
        report("created", path)
        return "created"
    existing = path.read_text()
    if existing == new_pointer:
        report("already present", path)
        return "unchanged"
    if not POINTER_PATTERN.match(existing.strip() + "\n"):
        report("conflict", path, "exists with non-pointer content — left untouched")
        return "refused_foreign"
    if has_uncommitted_changes(project_root, path):
        report("conflict", path, "pointer update needed but file has uncommitted changes — left untouched")
        return "refused_modified"
    path.write_text(new_pointer)
    report("updated", path, f"pointer now {new_pointer.strip()}")
    return "rewrote"


def has_uncommitted_changes(project_root: Path, path: Path) -> bool:
    result = subprocess.run(
        ["git", "status", "--porcelain", "--", str(path.relative_to(project_root))],
        cwd=project_root, capture_output=True, text=True,
    )
    status = result.stdout
    if not status:
        return False
    return status[:2] != "??"


def warn_if_legacy_layout(project_root: Path, pointer_outcome: str) -> None:
    legacy_agent_dir = project_root / "agent"
    legacy_changes_agents = project_root / "changes/agents"
    notes: list[str] = []

    if legacy_agent_dir.is_dir() and legacy_agent_dir.resolve() != AGENT_DIR.resolve():
        notes.append("  - delete the old folder:  [dim]rm -rf agent[/dim]")
        notes.append("  - remove any stale [dim]agent/[/dim] line from [dim].gitignore[/dim]")
    if legacy_changes_agents.is_dir():
        notes.append("  - delete the older folder:  [dim]rm -rf changes/agents[/dim]")
        notes.append("  - remove any stale [dim]changes/agents/[/dim] line from [dim].gitignore[/dim]")
    if pointer_outcome == "refused_modified":
        notes.append(
            "  - your [dim]CLAUDE.md[/dim] has uncommitted changes and was left untouched — "
            "update its pointer manually once resolved"
        )
    if pointer_outcome == "refused_foreign":
        notes.append(
            "  - your [dim]CLAUDE.md[/dim] contains unrecognised content and was left untouched — "
            "update its pointer manually"
        )

    if not notes:
        return

    console.print(
        "\n[bold yellow]Legacy layout detected.[/bold yellow] To finish migrating:\n"
        + "\n".join(notes)
    )


def report(status: str, path: Path, note: str = "") -> None:
    colours = {"created": "green", "updated": "cyan", "already present": "dim", "conflict": "yellow"}
    colour = colours.get(status, "white")
    label = f"[{colour}]{status:<15}[/{colour}]"
    detail = f"  [dim]{note}[/dim]" if note else ""
    console.print(f"  {label} {path}{detail}")


if __name__ == "__main__":
    if not os.environ.get("VIRTUAL_ENV"):
        print("Error: no virtual environment detected. Run this script via './opt-in' (requires uv), or activate a virtual environment first.")
        sys.exit(100)
    main()
