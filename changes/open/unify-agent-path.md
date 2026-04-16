# Unify agent path on `agent/`

## Intent

The agent's own instructions (`README.md`, `PROCESS.md`, `STYLE.md`, `MAP-GUIDANCE.md`, `ADDITIONAL/`) should live at the same path in this source repo and in projects that opt in. Today the source repo uses `agent/` while `opt-in.py` installs them to `changes/agents/` — two names for the same thing, and the installed location mixes agent docs into the `changes/` namespace which is otherwise reserved for per-change documents.

Unify on `agent/` everywhere.

## Approach

**Opt-in guard against self-install.** `opt-in.py` resolves its source path (`AGENT_DIR`) and destination path (`project_root / "agent"`) and refuses to run if they are equal. This is the direct expression of the hazard: the installer must not write onto its own source.

**Migration for existing opted-in projects.** Opt-in creates `agent/` as normal and, if it detects an existing `changes/agents/`, prints a warning telling the user to delete the old folder, remove the stale `.gitignore` entry, and update their `CLAUDE.md` reference. No automatic deletion or rewriting — keeps the tool simple and leaves state changes visible.

**Remove `migrate.py`.** The SPLIT→single migration era is closed. The script is dead weight and carries the old `changes/agents/` path reference — delete rather than update.

**Local cleanup of this source repo.** Delete the stale `changes/agents/` folder and remove its entry from `.gitignore`.

**Track `CLAUDE.md` in this source repo.** The source repo is a special case: it hosts the methodology and is always its own consumer, but the new self-install guard prevents it from regenerating its own `CLAUDE.md` through opt-in. Remove the `CLAUDE.md` entry from this repo's `.gitignore` so a fresh clone inherits the agent entry point. The rule still holds in target projects (where `CLAUDE.md` is a per-project artefact of opt-in) — this change is local to this repo.

**Archived change docs stay as written.** Two archives reference `changes/agents/`. They are historical records of the world at the time of those changes; rewriting them would erode the archive's value as a record.

## Plan

- [x] Update `agent/opt-in.py`: change destination path from `changes/agents` to `agent`, CLAUDE.md reference from `@changes/agents/README.md` to `@agent/README.md`, and gitignore entries list from `["CLAUDE.md", "changes/agents/"]` to `["CLAUDE.md", "agent/"]`.
- [x] Update `agent/opt-in.py`: add a self-install guard that refuses to run when resolved source (`AGENT_DIR`) equals resolved destination (`project_root / "agent"`).
- [x] Update `agent/opt-in.py`: detect an existing `changes/agents/` folder in the target project and print a warning listing the cleanup steps (delete the folder, remove the stale `.gitignore` line, update `CLAUDE.md` reference).
- [x] Remove `agent/migrate.py`.
- [x] Update root `README.md` line 9: "opt-in/migration scripts" → "opt-in script".
- [x] Remove `changes/agents/` line from `/root/cod/.gitignore`.
- [x] Delete the local `changes/agents/` folder.
- [x] Test: run `./opt-in` in this repo and confirm the self-install guard fires with a clear message.
- [x] Remove the `CLAUDE.md` line from this repo's `.gitignore` so the source repo's own `CLAUDE.md` is tracked.

## Conclusion

Reopened after archiving to address a gap: the self-install guard closed the path by which the source repo regenerated its own `CLAUDE.md`, leaving a fresh clone with no agent entry point. Fixed by tracking `CLAUDE.md` in this repo only. `CLAUDE.md` now shows as untracked-not-ignored; it is ready to be staged and committed by the user.

