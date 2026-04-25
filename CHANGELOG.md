# Changelog

Releases are listed in reverse-chronological order. Each entry names the version (the directory name under `changes/agent/`) and describes what changed and any manual migration steps.

## 2026-04-25

- `PROCESS.md` no longer hard-codes `agent/CHANGELOG.md`; refers to "the project's own changelog" and points at new `ADDITIONAL/CHANGELOG.md` (dated-`.N` or semver format options).
- `opt-in.py`: source CHANGELOG now read from repo root (was `agent/CHANGELOG.md`); install destination moves inside each version dir (`changes/agent/<version>/CHANGELOG.md`); legacy orphan at `changes/agent/CHANGELOG.md` is auto-removed on next install.

## 2026-04-24

- `PROCESS.md`: Feedback and Conclusion become post-approval summaries, drawn from a new build-time **Log** of the unexpected. The Changelog entry step folds into Completing. `README.md` startup states refreshed to match.

## 2026-04-22.5

- `PRINCIPLES.md`: **Joy** principle renamed to **Enjoyment** (Goal #2, principle section header and body, artifact-economy corollary). No change in substance — the rename softens the emotional register for better developer palatability.

## 2026-04-22.4

- `PROCESS.md`: trimmed five pieces of explanatory/disambiguation prose — user-review-rendered-file framing, "a well-constructed plan should not need close watching", the process-keyword-as-raw-material tail, and the two feedback-vs-aside disambiguation paragraphs.

## 2026-04-22.3

- `PROCESS.md`: new Build-mode paragraph requires bumping the smallest version increment whenever a build is handed to the user for review or test, so the user can visually confirm they're on the latest.

## 2026-04-22.2

- `PROCESS.md` **Approach** list gains a bullet: when a decision is fully carried by a proposed map node update, don't restate it in prose.

## 2026-04-22.1

- `MAP-GUIDANCE.md`: the only-child rule relaxed into an "only-child preference". Singleton children can remain as nodes if they represent a distinct concept or their detail would bloat the parent; the "if a sibling were added, would this still be a node?" test helps decide. The "Maintaining the map" signal updated to match.

## 2026-04-22

- `PROCESS.md` **Approach** guidance tightened: Approach is now framed as a list of decisions and their reasons, not a narrative. Added a short "what it is / isn't" list to discourage recap, file-by-file rehearsal, and subsections that don't carry a decision.

## 2026-04-19.1

- `opt-in.py` moved from `agent/opt-in.py` to the repo root. The script's internal `AGENT_DIR` was adjusted so it still finds the framework files under `agent/`. No downstream-visible effect.

## 2026-04-19

- Renamed `changes/process.md` to `changes/process-feedback.md`; file header updated to match.
- `opt-in.py` now reads the version name from the latest `## YYYY-MM-DD[.N]` heading in `agent/CHANGELOG.md` rather than computing from today's date. Every non-trivial completed change bumps the version by adding a new section at the top.
- `PROCESS.md` **Completing** section: added a Changelog entry step prompting the user on each change.
- `opt-in.py` no longer seeds a blank `changes/process-feedback.md` — the agent creates the file on first use of the `process:` keyword.

Downstream migration: after `opt-in.py` runs, any existing `changes/process.md` is left in place. Migrate entries manually with `git mv` to `changes/process-feedback.md` and delete the old file.

## 2026-04-18

Initial versioned release.

The framework introduces directory-based versioning under `changes/agent/<YYYY-MM-DD[.N]>/`. Previously, `opt-in.py` copied framework files to a single un-versioned `agent/` directory at the project root; now each install lands in a dated subdirectory and the project's `CLAUDE.md` is rewritten to point at it. Old versions are left in place so the user and agent retain direct access to prior installed state.

### Framework contents at this version

- **README.md** — startup behaviour, rules, permissions, map reference.
- **PROCESS.md** — plan/build lifecycle, Intent → Approach → Plan → Build → Archive; `process:` and `aside:` keywords.
- **STYLE.md** — coding and prose style principles.
- **MAP-GUIDANCE.md** — tree-of-nodes map format, Sync + Engagement rules, per-node pre-staging of map edits in an Approach.
- **ADDITIONAL/** — optional guides loaded on reference.

### Manual migration (from the un-versioned `agent/` layout)

After running `opt-in.py`:

- The new framework files are at `changes/agent/<YYYY-MM-DD[.N]>/`.
- `CLAUDE.md` now points at `@changes/agent/<YYYY-MM-DD[.N]>/README.md`.
- `.gitignore` has been updated to exclude `CLAUDE.md` and `changes/agent/`.
- The old `agent/` directory is left in place. Delete it manually (`rm -rf agent`) once you're satisfied the new layout works, and remove any stale `agent/` line from `.gitignore`.
