# Changelog reference points at the project's own changelog

## Intent

PROCESS.md's Completing section names `agent/CHANGELOG.md` as the file to update with a changelog entry after a build. This is the framework's own changelog — used by `opt-in.py` to derive the next install directory name — but when PROCESS.md is distributed into a downstream project, the instruction reads as "update the path `agent/CHANGELOG.md`", which doesn't exist there and shouldn't.

The framework project's own changelog should move to the repo root — the conventional place for a project changelog — and `opt-in.py` should copy it into the installed `agent/` folder so each install remains a complete snapshot. PROCESS.md's changelog step then refers to "the project's own changelog" generically, with the framework-specific version-naming mechanics (the `.N` convention, the "heading becomes install directory name" rule) stated as framework-local rather than universal.

## Approach

### Move the framework's CHANGELOG to the repo root

`agent/CHANGELOG.md` moves to `./CHANGELOG.md`. The file itself doesn't change — only its location and its conceptual role. Keeping it at repo root makes its identity clear: it is this project's own changelog, not an artifact that belongs inside the agent framework's distributable directory.

### `opt-in.py` reads from root, copies into the version dir

`opt-in.py` currently reads `AGENT_DIR / "CHANGELOG.md"` for version detection and copies the same file into the downstream project at `changes/agent/CHANGELOG.md` — an orphan sibling of the version directories. Two updates:

- The source path becomes the script's sibling `./CHANGELOG.md`.
- The install destination moves inside the version dir: `changes/agent/<version>/CHANGELOG.md`. Each installed version is then a self-contained framework snapshot, complete with its changelog-as-of-install-time.

The orphan `changes/agent/CHANGELOG.md` in existing downstream projects: `opt-in.py` removes it on next install if found (it's been fully superseded by the in-version copy), and emits a note. This parallels the `warn_if_legacy_layout` pattern already in the script.

### PROCESS.md refers to the project's changelog generically

The Completing subsection drops its `agent/CHANGELOG.md` mentions and the `.N`-and-install-directory-name details. It reads roughly: "If the change is substantive and the project maintains a changelog, draft a one-line entry for it (see `ADDITIONAL/CHANGELOG.md` for a recommended format)." No path; no framework-specific rules. A project without a changelog skips the step.

### General changelog guidance goes to `ADDITIONAL/CHANGELOG.md`

A new optional guide `agent/ADDITIONAL/CHANGELOG.md` covers when and how to maintain a changelog. It opens by acknowledging that projects vary: if the project has an established format, use that. Otherwise the guide recommends two options — a dated `## YYYY-MM-DD[.N]` format (simple, append-only, good for projects without formal releases) or a semver-based format (better when the project cuts versioned releases). Each option comes with a brief note on when it fits and how to write an entry. Listed in `ADDITIONAL/README.md` alongside the other optional guides.

### Framework-local coupling noted in root README

One piece is genuinely specific to this project: this framework uses the dated `.N` format (per the ADDITIONAL guide) and `opt-in.py` reads the topmost `## YYYY-MM-DD[.N]` heading of `./CHANGELOG.md` to derive the install directory name. That coupling, plus "this project's changelog is at `./CHANGELOG.md`", goes into root `README.md` as a short section. A fresh agent working in the framework repo finds the convention there.

### Naming stays `CHANGELOG.md`

Inside the version dir, the filename `CHANGELOG.md` is unambiguous — its scope is the framework snapshot it lives in. A downstream project's own `CHANGELOG.md` (if they keep one) lives at their repo root; no collision.

## Plan

- [x] Move `agent/CHANGELOG.md` to `./CHANGELOG.md` at repo root
- [x] Update `opt-in.py`: read source CHANGELOG from repo root (script sibling) instead of `AGENT_DIR`; install destination moves to `<version_dir>/CHANGELOG.md`; update the "Release notes" console line; remove the legacy `changes/agent/CHANGELOG.md` orphan if found on next install, with a note
- [x] Rewrite PROCESS.md's Completing subsection to drop the hard-coded `agent/CHANGELOG.md` path and the framework-specific heading-format / install-directory-name rules; point to `ADDITIONAL/CHANGELOG.md` for format guidance
- [x] Create `agent/ADDITIONAL/CHANGELOG.md` — acknowledges local conventions, otherwise recommends dated `.N` or semver, with a when-it-fits note and entry-writing guidance for each
- [x] Add the new guide to `agent/ADDITIONAL/README.md`
- [x] Add a short section to root `README.md` stating this project's changelog lives at `./CHANGELOG.md`, follows the dated `.N` format, and is read by `opt-in.py` (top heading → install directory name)
- [x] `grep` for any other references to `agent/CHANGELOG.md` or the old `changes/agent/CHANGELOG.md` path and update

## Log

- Implemented the legacy-orphan cleanup as auto-remove (per the Approach's literal wording "removes it on next install"), not warn-only. This departs slightly from the existing `warn_if_legacy_layout` behaviour, which advises but never deletes. The file being removed (`changes/agent/CHANGELOG.md`) has no user-edit expectation — it's always been opt-in-overwritten — so auto-remove seems safe, but worth confirming.
- Auto-remove confirmed by user during review; output is a single stdout line via the existing `report` helper, visually similar to the "created"/"updated" lines.

## Conclusion

Completed.

Proposed changelog entry:

```
## 2026-04-24.1

- `PROCESS.md` no longer hard-codes `agent/CHANGELOG.md`; refers to "the project's own changelog" and points at new `ADDITIONAL/CHANGELOG.md` (dated-`.N` or semver format options).
- `opt-in.py`: source CHANGELOG now read from repo root (was `agent/CHANGELOG.md`); install destination moves inside each version dir (`changes/agent/<version>/CHANGELOG.md`); legacy orphan at `changes/agent/CHANGELOG.md` is auto-removed on next install.
```
