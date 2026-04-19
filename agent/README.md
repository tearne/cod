# Agent Configuration

## On startup

Always do these steps at the start of every session:

1. Scan `changes/open/` and determine the state of each change:
   - **Intent only** — planning, needs Approach
   - **Intent + Approach** — planning, needs Plan
   - **Intent + Approach + Plan** — ready to build, or awaiting plan approval
   - **Has Feedback but no Conclusion** — needs replanning
   - **Has Feedback and Conclusion** — build complete, review documentation impact
   - **`active.md` exists** — a build is in progress or was interrupted

2. Inspect `changes/agent/` to identify the active framework version (the one this file's path belongs to) and any other versioned directories alongside it. If other versions exist, note them — the user may want a summary of what changed. Do not read `CHANGELOG.md` unprompted; surface it only when asked.

3. Announce your mode (plan or build) based on what you found.

4. Report the scan results, any additional version directories, and propose next steps to the user.

## Rules

Never do these without explicit user instruction:

- Git write operations (commit, push, branch, reset)
- Any change management decision: starting, advancing, or archiving a change
- Writing or editing any project file without an active change recorded in `changes/open/active.md`

Exempt from the active change requirement:

- Reading any project file
- Creating or editing files inside `changes/`
- Editing `map.md` — edits describing existing reality are permitted without an active change; edits describing pending work defer to Build via an active change. Always negotiated with the user, one node at a time. See MAP-GUIDANCE.md for the full rules.

## Map

If the project has a `map.md`, it is the primary frame of reference for understanding and describing changes. If no `map.md` exists, use whatever project documentation is available. See MAP-GUIDANCE.md for all map conventions.

## Changes

- `changes/open/` — open changes and the `active.md` lock file
- `changes/archive/` — completed changes, named `YYYY-MM-DD-<name>.md`
- `ADDITIONAL/` — optional guides, loaded on reference. See its README for the list.

@PROCESS.md
@STYLE.md
@MAP-GUIDANCE.md
