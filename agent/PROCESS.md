# Process

Two modes: **plan** and **build**. Each change moves through a fixed sequence with explicit user gates.


## Modes

**Plan mode** — research, reason, produce a change document. Read any project file. Write only to `changes/`. Negotiate structure and approach with the user through a drafted document and an Unresolved list of open items.

**Build mode** — execute an approved plan. Write to project files. Follow the plan; don't redesign. If the plan turns out to be wrong, stop and move the change to feedback rather than improvising.

Start in plan mode. Transition to build requires explicit user approval of the completed plan. No transition back — if building reveals a planning problem, the change returns to plan mode via the feedback mechanism. When a change returns to plan mode, the user decides whether to re-open the Approach or revise only the Plan. The Feedback section's Notes should surface enough detail for that decision.


## Plan mode

A change document is a single markdown file in `changes/open/`. It grows through three stages, each gated by user approval.

For each stage, the agent writes the draft into the change document and then asks for approval. The user reviews the rendered file (with the help of their editor's diff view), not a chat-rendered draft. Chat is used to disclose what needs attention — notably the Unresolved list described below — and to summarise what is ready for review.

If a `map.md` exists, it is the primary frame of reference. Describe the change in terms of the map's concepts and boundaries — not source files, not code structure. Tasks that affect mapped concepts reference the map node, not the implementing file.

### Intent

Why the change is needed. Domain language — what the user wants, not how the agent will do it. Brief. Ask the user to approve before continuing.

### Approach

How the change will be implemented. Read the codebase. If a map exists, read it to understand the affected area and identify coverage gaps. Map edits that describe the proposed change are deferred to Build and executed as Plan tasks; pre-stage them in the Approach per `MAP-GUIDANCE.md`. Map edits that bring the map in line with existing code (stale catch-ups) remain permitted at any time.

Once Intent is approved, the agent writes the full Approach into the change document, resolving everything it can on its own. Alongside the Approach, the agent writes an **Unresolved** section at the end of the document — a short bulleted list of the items the agent cannot settle alone, each pointing to the part of the Approach it affects.

After writing, the agent discloses the Unresolved list in chat so the user can answer immediately without opening the file. The user reviews the draft and answers the items (inline reply is fine). The agent folds the answers back into the Approach prose and removes resolved items from the list. When the list is empty, the Approach is ready for the user's explicit approval.

If the user disagrees with something the agent had already settled, they raise it like a new item. The agent folds the resolution in and adds new Unresolved items for any downstream choices now reopened.

The Unresolved section is deleted once the Plan is written — its absence signals that the Approach is settled.

### Plan

A concrete task list. Each task is a checklist item (add, update, remove, test). Map update tasks sit alongside implementation tasks — same list, same execution. Ask the user to approve.


## Build mode

### Entering build

On Plan approval, create `changes/open/active.md` containing the filename of the change (e.g. `tighten-agent-instructions.md`, with no path prefix). This is the lock — only one change builds at a time. If `active.md` already exists, stop and tell the user. An agent resuming an interrupted build reads the change document itself to find the next unticked task.

### Executing

Work through plan tasks in order. Tick each in the change document as it completes. Follow the plan; don't redesign mid-build.

Post concise progress updates on screen as the work proceeds, but do not pause for interaction task by task. Only interact mid-build when something warrants it: surprises, ambiguity, or a plan problem. A well-constructed plan should not need close watching.

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

### Changelog entry

After the Conclusion is approved and before the change is archived, the agent asks whether the change warrants an entry in `agent/CHANGELOG.md`. Trivial edits (typo fixes, minor doc wording) may not. For anything substantive, the agent drafts a one-line entry, surfaces it in chat for approval or reword, then adds a new `## YYYY-MM-DD[.N]` section at the top of `agent/CHANGELOG.md` with the entry beneath.

`.N` increments when today already has a section. The version name is the source of truth for the next `opt-in.py` install — the changelog heading becomes the target's directory name.


## Gates and permissions

**Approval** — only valid when the user gives a clear affirmative in direct response to the agent asking — e.g. "approved", "yes", "y", "ok", "go ahead", "sounds good". Silence, ambiguity, or tangential replies are not approval; neither is a message that raises new questions or concerns.

**Write permissions**
- Plan mode: write only to `changes/`. Reading any project file is always permitted.
- Build mode: write to project files and `changes/`.

**Git** — write operations (commit, push, branch) require explicit user instruction. Never commit or push on own initiative.


## Keywords

### Process keyword

At any point in a session the user may start a message with `process:` to capture an observation about the agent or the change process itself. These observations are raw material for later reflection — they feed back into the COD methodology when the user reviews them, not into the current task.

On a `process:` message, the agent:

- Appends a dated entry to `changes/process-feedback.md`, creating the file with a `# Process feedback` header if it doesn't yet exist. The entry is the observation plus whatever context (mode, active change, preceding topic, relevant file) would be lost otherwise. It need not be verbatim; the agent may tighten or rephrase to make the entry readable on its own later.
- Confirms capture in a single line.
- Returns to whatever task was under way without acting on the observation.

`changes/process-feedback.md` is a single append-only file, tracked in git, shared between collaborators. Its name echoes the build-stage **Feedback** section inside change documents, but the mechanism is distinct: this file is user-submitted observations about the methodology; Feedback sections are agent-written signals that a plan turned out wrong.


### Aside keyword

At any point in a session the user may use `aside:` (most naturally at the start of a message; other natural forms are also recognised) to park a topic for later without breaking the current flow.

On an aside, the agent:

- Dispatches the topic. **New proposal** (a fresh `changes/open/<slug>.md` with the captured text as Intent) if the topic is independent of the current discussion or no active discussion exists. **In-proposal aside** (appended to an "Asides" subsection at the end of the current change document) if the topic is within the scope of an in-progress change. The agent decides based on scope; when genuinely unsure, asks.
- Acknowledges placement in a single line ("Captured as new proposal: …" or "Added to asides in current change: …").
- Returns to whatever task was under way.

In-proposal asides during Intent/Approach/Plan discussion fold into the change as planning proceeds. In-proposal asides during Build sit until Conclusion time, when the user decides their fate (fold into Conclusion, spin off as new proposals, or discard). They are distinct from `Feedback` — Feedback is agent-written and signals that the plan turned out wrong; asides are user-parked thoughts that do not block execution.
