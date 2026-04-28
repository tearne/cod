# Agent Configuration

## On startup

Always do these steps at the start of every session:

1. Scan `changes/open/` and determine the state of each change:
   - **Intent only** — planning, needs Approach
   - **Intent + Approach** — planning, needs Plan (Approach may still list Unresolved items)
   - **Intent + Approach + Plan** — ready to build, or awaiting plan approval
   - **`active.md` points here, tasks remain** — build in progress or was interrupted; read the Log
   - **`active.md` points here, all tasks ticked, no Conclusion** — build finished, awaiting wrap-up decision; read the Log
   - **No `active.md`, Plan partly done, Log records a blocker** — build hit an impasse, awaiting user direction
   - **Has Feedback but no Conclusion** — back in plan mode, needs replanning
   - **Has Conclusion** — build done (review documentation impact if not already captured)

2. Announce your mode (plan or build) based on what you found.

3. Report the scan results and propose next steps to the user.

## On version update

When the user reports the agent directory has been updated, identify the new and previous versions from `CLAUDE.md`'s `@` pointer — current value and prior value from git history. Read the new version's `CHANGELOG.md` (each version directory ships its own) for the entries between then and now, and surface migration concerns.

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
@KEYWORDS.md
