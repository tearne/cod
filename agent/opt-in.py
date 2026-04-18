#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# dependencies = ["rich"]
# ///

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

from rich.console import Console

VERSION = "1.0.0"

console = Console()

AGENT_DIR = Path(__file__).parent

LEGACY_CLAUDE_MD = "@changes/agents/README.md\n"
NEW_CLAUDE_MD = "@agent/README.md\n"


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

    agents_dir = project_root / "agent"

    if AGENT_DIR.resolve() == agents_dir.resolve():
        console.print(
            "[bold red]Error:[/bold red] refusing to run — source and destination resolve to the same path.\n"
            "This script is its own source of truth; running it here would install the agent files on top of themselves."
        )
        sys.exit(1)

    # Copy agent files
    for name in ["README.md", "PROCESS.md", "STYLE.md", "MAP-GUIDANCE.md"]:
        copy_asset(AGENT_DIR / name, agents_dir / name)

    # Copy ADDITIONAL directory
    additional_src = AGENT_DIR / "ADDITIONAL"
    additional_dest = agents_dir / "ADDITIONAL"
    if additional_src.is_dir():
        for f in sorted(additional_src.iterdir()):
            if f.is_file():
                copy_asset(f, additional_dest / f.name)

    # Project root CLAUDE.md pointing to agent README
    legacy_claude_md_outcome = rewrite_legacy_claude_md(project_root)
    create_file(project_root / "CLAUDE.md", NEW_CLAUDE_MD)

    # Exclude global CLAUDE.md so the project uses its own
    create_settings(
        project_root / ".claude" / "settings.local.json",
        excludes=["~/.claude/CLAUDE.md"],
    )

    # Create changes folder structure
    create_dir(project_root / "changes/open")
    create_dir(project_root / "changes/archive")

    # Update .gitignore
    update_gitignore(project_root / ".gitignore")

    warn_if_legacy_layout(project_root, legacy_claude_md_outcome)

    console.print("\n[bold green]Done.[/bold green]")


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
    entries = ["CLAUDE.md", "agent/"]
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


def rewrite_legacy_claude_md(project_root: Path) -> str:
    path = project_root / "CLAUDE.md"
    if not path.exists() or path.read_text() != LEGACY_CLAUDE_MD:
        return "inapplicable"
    if has_uncommitted_changes(project_root, path):
        report("conflict", path, "legacy pointer detected but file has uncommitted changes — left untouched")
        return "refused_modified"
    path.write_text(NEW_CLAUDE_MD)
    report("updated", path, "rewrote legacy pointer to @agent/README.md")
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


def warn_if_legacy_layout(project_root: Path, claude_md_outcome: str) -> None:
    legacy_dir = project_root / "changes/agents"
    if not legacy_dir.exists():
        return
    steps = [
        "  - delete the old folder:  [dim]rm -rf changes/agents[/dim]",
        "  - remove the stale line [dim]changes/agents/[/dim] from [dim].gitignore[/dim]",
    ]
    if claude_md_outcome == "refused_modified":
        steps.append(
            "  - update your [dim]CLAUDE.md[/dim] reference from [dim]@changes/agents/README.md[/dim] to [dim]@agent/README.md[/dim] "
            "(left untouched because it has uncommitted changes)"
        )
    console.print(
        "\n[bold yellow]Legacy layout detected:[/bold yellow] [dim]changes/agents/[/dim]\n"
        "The agent files now live at [bold]agent/[/bold]. To finish migrating:\n"
        + "\n".join(steps)
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
