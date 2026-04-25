# Process

Two modes: **plan** and **build**. Each change moves through a fixed sequence with explicit user gates.


## Modes

**Plan mode** — research, reason, produce a change document. Read any project file. Write only to `changes/`. Negotiate structure and approach with the user through a drafted document and an Unresolved list of open items.

**Build mode** — execute an approved plan. Write to project files. Follow the plan; don't redesign. If the plan turns out to be wrong, stop and hand back to the user for direction rather than improvising.

Start in plan mode. Transition to build requires explicit user approval of the completed plan. No transition back — if building reveals a planning problem, the change returns to plan mode after the user agrees that replanning is needed. When a change returns to plan mode, the user decides whether to re-open the Approach or revise only the Plan. The Feedback section's Notes (written after that agreement) should surface enough detail for that decision.


## Plan mode

A change document is a single markdown file in `changes/open/`. It grows through three stages, each gated by user approval.

For each stage, the agent writes the draft into the change document and then asks for approval. The user reviews the rendered file (with the help of their editor's diff view), not a chat-rendered draft. Chat is used to disclose what needs attention — notably the Unresolved list described below — and to summarise what is ready for review.

If a `map.md` exists, it is the primary frame of reference. Describe the change in terms of the map's concepts and boundaries — not source files, not code structure. Tasks that affect mapped concepts reference the map node, not the implementing file.

### Intent

Why the change is needed. Domain language — what the user wants, not how the agent will do it. Brief. Ask the user to approve before continuing.

### Approach

How the change will be implemented. Read the codebase. If a map exists, read it to understand the affected area and identify coverage gaps. Map edits that describe the proposed change are deferred to Build and executed as Plan tasks; pre-stage them in the Approach per `MAP-GUIDANCE.md`. Map edits that bring the map in line with existing code (stale catch-ups) remain permitted at any time.

Once Intent is approved, the agent writes the Approach into the change document. Treat it as a list of decisions and their reasons, not a narrative:

- One subsection per decision; self-evident choices don't need a subsection.
- State the decision, then the reason in a sentence or two. Stop.
- Don't recap the Intent. Don't rehearse code structure or file-by-file steps — those belong in the Plan.
- When a decision is fully carried by a proposed map node update, don't restate it in prose — the node is the decision. Prose is for decisions that aren't in a node, or for the "why" the node can't convey.
- If a subsection can be deleted without losing a decision, delete it.

Alongside the Approach, the agent writes an **Unresolved** section at the end of the document — a short bulleted list of the items the agent cannot settle alone, each pointing to the part of the Approach it affects.

After writing, the agent discloses the Unresolved list in chat so the user can answer immediately without opening the file. The user reviews the draft and answers the items (inline reply is fine). The agent folds the answers back into the Approach prose and removes resolved items from the list. When the list is empty, the Approach is ready for the user's explicit approval.

If the user disagrees with something the agent had already settled, they raise it like a new item. The agent folds the resolution in and adds new Unresolved items for any downstream choices now reopened.

The Unresolved section is deleted once the Plan is written — its absence signals that the Approach is settled.

### Plan

A concrete task list. Each task is a checklist item (add, update, remove, test). Map update tasks sit alongside implementation tasks — same list, same execution. Ask the user to approve.


## Build mode

### Entering build

On Plan approval, create `changes/open/active.md` containing the filename of the change (e.g. `tighten-agent-instructions.md`, with no path prefix). This is the lock — only one change builds at a time. If `active.md` already exists, stop and tell the user. An agent resuming an interrupted build reads the change document itself to find the next unticked task.

### Log

During build, the agent maintains a running **Log** at the bottom of the change document — a bulleted list of the unexpected. Surprises, blockers, deviations, partial progress, or anything worth remembering between sessions that the ticked plan tasks don't already convey. Routine execution going to plan does not need logging.

Most recent entry at the bottom; one or two sentences each. The agent adds to the Log during build without user prompting, but only when something warrants it.

The Log is working memory, not a signal that the plan turned out wrong. It is preserved when the change is archived — the archive is the complete record.

### Executing

Work through plan tasks in order. Tick each in the change document as it completes. Follow the plan; don't redesign mid-build.

Post concise progress updates on screen as the work proceeds, but do not pause for interaction task by task. Only interact mid-build when something warrants it: surprises, ambiguity, or a plan problem. A well-constructed plan should not need close watching.

Minor surprises — unexpected details that don't break the plan — go in the Log, and the build continues.

If the plan is wrong or incomplete and the path forward is unclear: stop, note the blocker in the Log, remove `active.md`, tell the user. Do not write Feedback yet — that comes after the user has agreed the change needs replanning.

### Feedback

Feedback is written only after the user has agreed that the plan needs revisiting. The agent drafts it from the Log plus the user's direction. It has three parts:

- **Status:** implemented / partially implemented / not implemented
- **Notes:** what came up, what's unclear, and — for partial or not implemented — what the planner should reconsider
- **Documentation impact:** any project documents that may need review (e.g. map, spec, README)

Markers:

- Conclusion present → change is done.
- Feedback present without Conclusion → change is back in plan mode, awaiting replanning.

### Completing

When all plan tasks are done, tell the user and ask them to review. The Log is the record the user reads; highlight anything notable in chat. Do not write the Conclusion yet.

On the user's confirmation that the build is done, draft the Conclusion. It comments only on what isn't already captured — deviations, docs touched, or surprises. If nothing new, "Completed." suffices. If the change is substantive (not a typo or minor doc fix) and the project maintains a changelog, the draft also proposes an entry for it (see `ADDITIONAL/CHANGELOG.md` for a recommended format if the project hasn't established one).

Surface the draft for approval. On approval:

- If a changelog entry was approved, add it to the project's changelog.
- Move the change file to `changes/archive/` (prefixed `YYYY-MM-DD-<name>.md`).
- Remove `active.md`.


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

`changes/process-feedback.md` is a single append-only file, tracked in git, shared between collaborators. Its name echoes the build-stage **Feedback** section inside change documents, but the mechanism is distinct: this file is user-submitted observations about the methodology; Feedback sections are agent-written summaries (post-approval) recording that a plan turned out wrong.


### Aside keyword

At any point in a session the user may use `aside:` (most naturally at the start of a message; other natural forms are also recognised) to park a topic for later without breaking the current flow.

On an aside, the agent:

- Dispatches the topic. **New proposal** (a fresh `changes/open/<slug>.md` with the captured text as Intent) if the topic is independent of the current discussion or no active discussion exists. **In-proposal aside** (appended to an "Asides" subsection at the end of the current change document) if the topic is within the scope of an in-progress change. The agent decides based on scope; when genuinely unsure, asks.
- Acknowledges placement in a single line ("Captured as new proposal: …" or "Added to asides in current change: …").
- Returns to whatever task was under way.

In-proposal asides during Intent/Approach/Plan discussion fold into the change as planning proceeds. In-proposal asides during Build sit until Conclusion time, when the user decides their fate (fold into Conclusion, spin off as new proposals, or discard). They are distinct from `Feedback` — Feedback is an agent-written summary (post-approval) recording that the plan turned out wrong; asides are user-parked thoughts that do not block execution.
