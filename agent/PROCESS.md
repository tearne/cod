# Process

Two modes: **plan** and **build**. Each change moves through a fixed sequence with explicit user gates.


## Modes

**Plan mode** — research, reason, produce a change document. Read any project file. Write only to `changes/`. Fine-grained back-and-forth with the user on structure and approach.

**Build mode** — execute an approved plan. Write to project files. Follow the plan; don't redesign. If the plan turns out to be wrong, stop and move the change to feedback rather than improvising.

Start in plan mode. Transition to build requires explicit user approval of the completed plan. No transition back — if building reveals a planning problem, the change returns to plan mode via the feedback mechanism.


## Plan mode

A change document is a single markdown file in `changes/open/`. It grows through three stages, each gated by user approval.

If a `map.md` exists, it is the primary frame of reference. Describe the change in terms of the map's concepts and boundaries — not source files, not code structure. Tasks that affect mapped concepts reference the map node, not the implementing file.

### Intent

Why the change is needed. Domain language — what the user wants, not how the agent will do it. Brief. Ask the user to approve before continuing.

### Approach

How the change will be implemented. Read the codebase. If a map exists, read it to understand the affected area and identify coverage gaps.

One topic per message. Show the pending queue:

**Pending**
1. topic B
2. topic C

**Current**
What should we do about topic A?

Wait for the user's response before moving to the next topic. Ask the user to approve the Approach before continuing.

### Plan

A concrete task list. Each task is a checklist item (add, update, remove, test). Map update tasks sit alongside implementation tasks — same list, same execution. Ask the user to approve.


## Build mode

### Entering build

On Plan approval, create `changes/open/active.md` containing the name of the change file. This is the lock — only one change builds at a time. If `active.md` already exists, stop and tell the user.

### Executing

Work through plan tasks in order. Tick each as it completes. Follow the plan; don't redesign mid-build.

If the plan is wrong or incomplete and the path forward is unclear: stop, write a Feedback section explaining what was found and what needs replanning, remove `active.md`, tell the user. The change returns to plan mode.

If the surprise is minor and the path forward is clear: continue, but write a Feedback section noting what was unexpected. Review for map impact when the change completes.

- Feedback without Conclusion → needs replanning.
- Feedback with Conclusion → build done, review for map impact.

### Completing

When all tasks are done, write a Conclusion section summarising what was done and any deviations. Ask the user to review. On approval, move the change file to `changes/archive/` (prefixed `YYYY-MM-DD-<name>.md`), remove `active.md`.


## Gates and permissions

**Approval** — only valid when the user says "approved", "yes", or "y" in direct response to the agent asking. Silence, ambiguity, or tangential replies are not approval.

**Write permissions**
- Plan mode: write only to `changes/`. Reading any project file is always permitted.
- Build mode: write to project files and `changes/`.

**Git** — write operations (commit, push, branch) require explicit user instruction. Never commit or push on own initiative.
