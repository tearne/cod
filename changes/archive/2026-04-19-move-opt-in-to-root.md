# Move opt-in script to project root

## Intent

The opt-in script currently lives at `agent/opt-in.py`, alongside the framework documents it installs. Consider moving it to the project root (e.g. `opt-in.py` or `./opt-in`) so it's the first thing a new contributor sees and can be run without descending into `agent/`. The script's role is "set this project up" — which belongs at the entry point of the repo, not inside the directory of assets it copies.

## Approach

### Move

`git mv agent/opt-in.py opt-in.py` — single-file move. The script stays executable via its existing shebang.

### Script internal: locating `agent/`

The script currently uses `AGENT_DIR = Path(__file__).parent` because it sits inside `agent/`. After the move the script sits one level up, so change to `AGENT_DIR = Path(__file__).parent / "agent"`. All reads of framework files (`README.md`, `PROCESS.md`, `STYLE.md`, `MAP-GUIDANCE.md`, `ADDITIONAL/`, `CHANGELOG.md`) flow through `AGENT_DIR` and need no further change.

The self-install guard (`AGENT_DIR.resolve() == (project_root / "agent").resolve()`) continues to work after the `AGENT_DIR` adjustment — in the source repo the two still collapse to the same path and the script refuses to run.

### Documentation updates

- `README.md` at repo root: line describing `agent/` as containing "process files, style guides, map guidance, and opt-in script" — drop "and opt-in script" and mention the script at root-level.

### Changelog

Add a new entry to `agent/CHANGELOG.md` under a fresh `## 2026-04-19.1` section (today already has a `2026-04-19` from the rename change), noting the move. No downstream migration needed — the script's location is a source-repo detail; downstream projects only see its effects.

## Plan

- [x] `git mv agent/opt-in.py opt-in.py`
- [x] Update `opt-in.py`: change `AGENT_DIR = Path(__file__).parent` to `AGENT_DIR = Path(__file__).parent / "agent"`
- [x] Update `README.md` at repo root — adjust the `agent/` bullet and mention `opt-in.py` at root
- [x] Test: run `./opt-in.py` from the source repo; verify the self-install guard still fires
- [x] Test: run `/root/cod/opt-in.py` against a fresh scratch project; verify install succeeds and framework files land in the versioned directory
- [x] At Conclusion time: draft changelog entry, prompt user, add `## 2026-04-19.1` section to `agent/CHANGELOG.md`

## Conclusion

Completed.

