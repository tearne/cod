#!/usr/bin/env -S uv run --script --
# /// script
# requires-python = "==3.12.*"
# dependencies = ["rich"]
# ///

"""Migrate a project from the SPLIT agent system to the single-agent system.

Assumes opt-in.py has already been run — refuses if the new structure
is not in place.
"""

import os
import subprocess
import sys
from pathlib import Path

from rich.console import Console

VERSION = "1.0.0"

console = Console()


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
    project_root = git_root()

    if not (project_root / "changes/agents/README.md").exists():
        console.print("[bold red]Error:[/bold red] new agent structure not found. Run opt-in.py first.")
        sys.exit(1)

    console.print(f"Migrating [bold]{project_root}[/bold] from SPLIT to single-agent\n")

    # Move open changes from old state machine folders into changes/open/
    for folder in ["planning", "ready", "feedback", "interrupted"]:
        move_contents(
            project_root / "changes/active" / folder,
            project_root / "changes/open",
        )

    # Remove old active directory if empty
    remove_if_empty(project_root / "changes/active")

    # Remove old agent directories
    for role in ["supervisor", "planner", "builder"]:
        remove_tree(project_root / "changes/agents" / role)

    # Remove launcher scripts
    for launcher in ["supervisor_start.py", "changes/agents/planner_start.py", "changes/agents/builder_start.py"]:
        remove_file(project_root / launcher)

    # Update CLAUDE.md to point to the new agent README
    claude_md = project_root / "CLAUDE.md"
    new_ref = "@changes/agents/README.md\n"
    if claude_md.exists():
        content = claude_md.read_text()
        if content == new_ref:
            report("already present", claude_md)
        else:
            claude_md.write_text(new_ref)
            report("updated", claude_md, f"→ {new_ref.strip()}")

    # Update .gitignore — remove old entries
    update_gitignore(project_root / ".gitignore")

    console.print("\n[bold green]Migration complete.[/bold green]")


def move_contents(src: Path, dest: Path) -> None:
    if not src.exists():
        return
    for item in src.iterdir():
        target = dest / item.name
        if target.exists():
            report("conflict", item, f"destination {target} already exists — left untouched")
        else:
            item.rename(target)
            report("moved", item, f"→ {target}")
    remove_if_empty(src)


def remove_tree(path: Path) -> None:
    if not path.exists():
        return
    for item in sorted(path.rglob("*"), reverse=True):
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            item.rmdir()
    path.rmdir()
    report("removed", path)


def remove_file(path: Path) -> None:
    if not path.exists():
        return
    path.unlink()
    report("removed", path)


def remove_if_empty(path: Path) -> None:
    if not path.exists():
        return
    if any(path.iterdir()):
        report("kept", path, "not empty")
        return
    path.rmdir()
    report("removed", path)


def update_gitignore(path: Path) -> None:
    if not path.exists():
        return
    content = path.read_text()
    lines = content.splitlines()
    old_entries = ["supervisor_start.py", "planner/", "builder/"]
    to_remove = [e for e in old_entries if e in lines]
    if not to_remove:
        return
    lines = [l for l in lines if l not in to_remove]
    path.write_text("\n".join(lines) + ("\n" if lines else ""))
    report("updated", path, f"removed: {', '.join(to_remove)}")


def report(status: str, path: Path, note: str = "") -> None:
    colours = {"moved": "cyan", "removed": "dim", "updated": "cyan", "conflict": "yellow", "kept": "yellow"}
    colour = colours.get(status, "white")
    label = f"[{colour}]{status:<15}[/{colour}]"
    detail = f"  [dim]{note}[/dim]" if note else ""
    console.print(f"  {label} {path}{detail}")


if __name__ == "__main__":
    if not os.environ.get("VIRTUAL_ENV"):
        print("Error: no virtual environment detected. Run this script via './migrate' (requires uv), or activate a virtual environment first.")
        sys.exit(100)
    main()
