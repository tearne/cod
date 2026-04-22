# Changelog

Releases are listed in reverse-chronological order. Each entry names the version (the directory name under `changes/agent/`) and describes what changed and any manual migration steps.

## 0.1.8

- `PROCESS.md`: trimmed five pieces of explanatory/disambiguation prose — user-review-rendered-file framing, "a well-constructed plan should not need close watching", the process-keyword-as-raw-material tail, and the two feedback-vs-aside disambiguation paragraphs.

## 0.1.7

- `agent/CHANGELOG.md` headings switched to semver (`X.Y.Z`). `opt-in.py` version regex updated accordingly; installs now land under `changes/agent/<semver>/`. `ADDITIONAL/VERSIONING.md` gains a line stating project changelog headings should match the project's versioning scheme.

## 0.1.6

- `PROCESS.md`: the **Changelog entry** step folded into **Conclusion** duties; new Build-mode paragraph prescribes patch-version bumps on every build hand-over for test (referencing `ADDITIONAL/VERSIONING.md`).

## 0.1.5

- `PROCESS.md` **Approach** list gains a bullet: when a decision is fully carried by a proposed map node update, don't restate it in prose.

## 0.1.4

- `MAP-GUIDANCE.md`: the only-child rule relaxed into an "only-child preference". Singleton children can remain as nodes if they represent a distinct concept or their detail would bloat the parent; the "if a sibling were added, would this still be a node?" test helps decide. The "Maintaining the map" signal updated to match.

## 0.1.3

- `PROCESS.md` **Approach** guidance tightened: Approach is now framed as a list of decisions and their reasons, not a narrative. Added a short "what it is / isn't" list to discourage recap, file-by-file rehearsal, and subsections that don't carry a decision.

## 0.1.2

- `opt-in.py` moved from `agent/opt-in.py` to the repo root. The script's internal `AGENT_DIR` was adjusted so it still finds the framework files under `agent/`. No downstream-visible effect.

## 0.1.1

- Renamed `changes/process.md` to `changes/process-feedback.md`; file header updated to match.
- `opt-in.py` now reads the version name from the latest version heading in `agent/CHANGELOG.md` rather than computing from today's date. Every non-trivial completed change bumps the version by adding a new section at the top.
- `PROCESS.md` **Completing** section: added a Changelog entry step prompting the user on each change.
- `opt-in.py` no longer seeds a blank `changes/process-feedback.md` — the agent creates the file on first use of the `process:` keyword.

Downstream migration: after `opt-in.py` runs, any existing `changes/process.md` is left in place. Migrate entries manually with `git mv` to `changes/process-feedback.md` and delete the old file.

## 0.1.0

Initial versioned release.

The framework introduces directory-based versioning under `changes/agent/<version>/`. Previously, `opt-in.py` copied framework files to a single un-versioned `agent/` directory at the project root; now each install lands in a versioned subdirectory and the project's `CLAUDE.md` is rewritten to point at it. Old versions are left in place so the user and agent retain direct access to prior installed state.

### Framework contents at this version

- **README.md** — startup behaviour, rules, permissions, map reference.
- **PROCESS.md** — plan/build lifecycle, Intent → Approach → Plan → Build → Archive; `process:` and `aside:` keywords.
- **STYLE.md** — coding and prose style principles.
- **MAP-GUIDANCE.md** — tree-of-nodes map format, Sync + Engagement rules, per-node pre-staging of map edits in an Approach.
- **ADDITIONAL/** — optional guides loaded on reference.

### Manual migration (from the un-versioned `agent/` layout)

After running `opt-in.py`:

- The new framework files are at `changes/agent/<version>/`.
- `CLAUDE.md` now points at `@changes/agent/<version>/README.md`.
- `.gitignore` has been updated to exclude `CLAUDE.md` and `changes/agent/`.
- The old `agent/` directory is left in place. Delete it manually (`rm -rf agent`) once you're satisfied the new layout works, and remove any stale `agent/` line from `.gitignore`.
