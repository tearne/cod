# Versioning and update notes

## Intent

The agent framework gets copied into projects via `opt-in.py`. As the framework evolves, projects need a way to know what version they're on, what's changed since they last updated, and what (if anything) requires their attention when picking up a newer version. Today there is no version marker, no changelog, and no per-release notes — so a project re-running `opt-in.py` gets new files with no sense of what moved, why, or whether any manual step is required.

This change introduces a version identifier for the framework and an update-notes mechanism, so projects have a clear bridge between the version they have and the version they're about to adopt.

## Approach

### Structure: versioned directories

In target projects, framework files live in versioned subdirectories under `changes/agent/`:

```
changes/
  agent/
    CHANGELOG.md
    2026-04-18/
      README.md
      PROCESS.md
      STYLE.md
      MAP-GUIDANCE.md
      ADDITIONAL/...
    2026-05-14/
      ...
  open/
  archive/
  process.md
```

The directory name *is* the version (`YYYY-MM-DD`, with `.N` suffix if multiple installs land on the same day). No separate `VERSION` file is needed.

The project's root `CLAUDE.md` points at the active version's README:

```
@changes/agent/2026-04-18/README.md
```

Old versions coexist alongside the current one until the user deletes them. Both the user and the agent have direct filesystem access to every previously installed state, which is the primary mechanism for comparing versions.

### Git treatment

`changes/agent/` and the project's root `CLAUDE.md` are gitignored in target projects, mirroring how `agent/` is treated today. Version comparison relies on the directories coexisting in the working tree, not on git history.

### Cumulative changelog

A single `changes/agent/CHANGELOG.md` carries the full history of releases in reverse-chronological order. Each entry names the version and describes what changed and any manual migration steps. The file sits outside the version directories because it is always the newest copy that is relevant — prior installs' changelogs are strict subsets.

The source repo maintains the master copy at `agent/CHANGELOG.md`; each release adds a new section at the top before `opt-in.py` is run against target projects.

### `opt-in.py` behaviour (kept dumb)

On install or re-install:

1. Compute target path: `changes/agent/<today>/` (or `<today>.N` if a directory for today already exists).
2. Copy framework files into it (`README.md`, `PROCESS.md`, `STYLE.md`, `MAP-GUIDANCE.md`, `ADDITIONAL/`).
3. Copy the source `CHANGELOG.md` to `changes/agent/CHANGELOG.md`, overwriting the target's existing copy.
4. Rewrite `CLAUDE.md` at project root to point at `@changes/agent/<new-version>/README.md`.
5. Leave old versioned directories in place.
6. Print the path to `changes/agent/CHANGELOG.md` on stdout so the user can open it immediately.

No version comparison, no changelog rendering — the script is purely mechanical. All interpretation is the agent's or user's job.

### Agent-side update awareness

On startup, after the existing `changes/open/` scan, the agent inspects `changes/agent/`. If more than one versioned directory is present, it notes the current version (the one `CLAUDE.md` points at) and the older versions alongside, and mentions them in its startup report so the user has the option of asking for a summary.

The agent does not auto-read `CHANGELOG.md` or force a migration summary — the heavy lifting only happens when the user asks ("what's new?", "what changed since 2026-03-01?"). At that point the agent reads `CHANGELOG.md`, and can diff directories if specifics matter.

### Source repo layout

The source COD repo keeps `agent/` as the working master — not `changes/agent/<version>/`. The versioning layout only applies to *target* projects. `opt-in.py` reads from the source `agent/` and writes into the versioned target path, stamping the version at install time.

### Handling the current layout

Existing installations have framework files at `agent/` (un-versioned) and `CLAUDE.md` pointing at `@agent/README.md`. The first `opt-in.py` run after this change lands will:

- Create `changes/agent/<today>/` with the current framework files.
- Rewrite `CLAUDE.md` from `@agent/README.md` to `@changes/agent/<today>/README.md`.
- Leave the legacy `agent/` directory in place; surface a hint on stdout reminding the user to remove it manually once they're satisfied the new layout is working.

### Document updates required

- Create `agent/CHANGELOG.md` (in the source repo) — the initial entry summarising the current state of the framework as v`2026-04-18`.
- Update `agent/opt-in.py`:
  - Write framework files to `changes/agent/<YYYY-MM-DD[.N]>/` instead of `agent/`.
  - Copy `CHANGELOG.md` to `changes/agent/CHANGELOG.md`.
  - Rewrite `CLAUDE.md` to point at the new versioned path.
  - Print the changelog path at the end of the run.
  - Add the legacy-cleanup hint when the old `agent/` directory is detected.
  - Ensure the project's `.gitignore` excludes `CLAUDE.md` and `changes/agent/` (add entries if missing).
- Update `agent/README.md` — add the startup step that reports the presence of multiple versioned directories in `changes/agent/`.

## Plan

- [x] Create `agent/CHANGELOG.md` with an initial entry summarising the current framework as v`2026-04-18`
- [x] Update `agent/opt-in.py`: compute versioned target path `changes/agent/<today>[.N]/`; copy framework files (`README.md`, `PROCESS.md`, `STYLE.md`, `MAP-GUIDANCE.md`, `ADDITIONAL/`) there instead of into `agent/`
- [x] Update `agent/opt-in.py`: copy `CHANGELOG.md` from source to `changes/agent/CHANGELOG.md`, overwriting any existing target copy
- [x] Update `agent/opt-in.py`: rewrite project root `CLAUDE.md` to `@changes/agent/<new-version>/README.md`, extending the existing uncommitted-changes guard to cover the `@agent/README.md` pointer case
- [x] Update `agent/opt-in.py`: change the `.gitignore` updater — add `changes/agent/`, keep `CLAUDE.md`, drop the obsolete `agent/` entry from the add-set
- [x] Update `agent/opt-in.py`: replace the legacy-layout warning so that when an un-versioned `agent/` directory is detected at repo root after migration, the hint tells the user to remove it manually when ready
- [x] Update `agent/opt-in.py`: print `changes/agent/CHANGELOG.md` path at the end of the run
- [x] Update `agent/README.md` startup section: add a step that inspects `changes/agent/`, identifies the version `CLAUDE.md` points at and any older versions alongside, and reports them in the scan output
- [x] Test: run `opt-in.py` against a fresh scratch project; verify versioned directory created, `CLAUDE.md` points at it, `.gitignore` entries present, changelog path printed
- [x] Test: run `opt-in.py` twice in the same day against a scratch project; verify `.N` suffix behaviour
- [x] Test: run `opt-in.py` against a project already on the `@agent/README.md` pointer layout; verify pointer rewrite and legacy hint appear

## Conclusion

Implemented. One small mid-build fix: the changelog copy initially reported "updated" on fresh installs because the existence check ran after the write — corrected to capture the state up-front.


