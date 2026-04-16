# Process

Two modes: **plan** and **build**. Each change moves through a fixed sequence with explicit user gates.


## Modes

**Plan mode** — research, reason, produce a change document. Read any project file. Write only to `changes/`. Fine-grained back-and-forth with the user on structure and approach.

**Build mode** — execute an approved plan. Write to project files. Follow the plan; don't redesign. If the plan turns out to be wrong, stop and move the change to feedback rather than improvising.

Start in plan mode. Transition to build requires explicit user approval of the completed plan. No transition back — if building reveals a planning problem, the change returns to plan mode via the feedback mechanism. When a change returns to plan mode, the user decides whether to re-open the Approach or revise only the Plan. The Feedback section's Notes should surface enough detail for that decision.


## Plan mode

A change document is a single markdown file in `changes/open/`. It grows through three stages, each gated by user approval.

If a `map.md` exists, it is the primary frame of reference. Describe the change in terms of the map's concepts and boundaries — not source files, not code structure. Tasks that affect mapped concepts reference the map node, not the implementing file.

### Intent

Why the change is needed. Domain language — what the user wants, not how the agent will do it. Brief. Ask the user to approve before continuing.

### Approach

How the change will be implemented. Read the codebase. If a map exists, read it to understand the affected area and identify coverage gaps.

Discuss one topic per message. In each message, show a **Pending** queue and the **Current** topic so the user sees how much is still unaddressed. The queue is a conversational device, not part of the change document — the Approach section records resolved outcomes.

**Pending**
1. topic B
2. topic C

**Current**
What should we do about topic A?

The agent drafts the initial topic list from reading the code and (if present) the map, and shows it before starting. Topics may be added, reordered, or dropped as discussion proceeds. Wait for the user's response before moving on. Ask the user to approve the Approach before continuing.

The grain size matters: many small decisions with the user's full attention, rather than one overwhelming list. Fine-grained negotiation belongs in planning — not building.

### Plan

A concrete task list. Each task is a checklist item (add, update, remove, test). Map update tasks sit alongside implementation tasks — same list, same execution. Ask the user to approve.


## Build mode

### Entering build

On Plan approval, create `changes/open/active.md` containing the filename of the change (e.g. `tighten-agent-instructions.md`, with no path prefix). This is the lock — only one change builds at a time. If `active.md` already exists, stop and tell the user. An agent resuming an interrupted build reads the change document itself to find the next unticked task.

### Executing

Work through plan tasks in order. Tick each as it completes. Follow the plan; don't redesign mid-build.

If the plan is wrong or incomplete and the path forward is unclear: stop, write a Feedback section, remove `active.md`, tell the user. The change returns to plan mode.

If the surprise is minor and the path forward is clear: continue, but write a Feedback section noting what was unexpected.

**Feedback** has three parts:

- **Status:** implemented / partially implemented / not implemented
- **Notes:** what came up, what's unclear, and — for partial or not implemented — what the planner should reconsider
- **Documentation impact:** any project documents that may need review (e.g. map, spec, README)

The two gates:

- Feedback without Conclusion → needs replanning.
- Feedback with Conclusion → build done.

### Completing

When all tasks are done, write a Conclusion section. Ask the user to review. On approval, move the change file to `changes/archive/` (prefixed `YYYY-MM-DD-<name>.md`), remove `active.md`.

**Conclusion** comments only on anything new — deviations, docs touched, or surprises not already captured in the change document. If nothing new, "Completed." suffices.


## Gates and permissions

**Approval** — only valid when the user gives a clear affirmative in direct response to the agent asking — e.g. "approved", "yes", "y", "ok", "go ahead", "sounds good". Silence, ambiguity, or tangential replies are not approval; neither is a message that raises new questions or concerns.

**Write permissions**
- Plan mode: write only to `changes/`. Reading any project file is always permitted.
- Build mode: write to project files and `changes/`.

**Git** — write operations (commit, push, branch) require explicit user instruction. Never commit or push on own initiative.
