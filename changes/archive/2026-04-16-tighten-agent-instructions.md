# Tighten Agent Instructions

## Intent

The agent instructions in `changes/agents/` have a handful of gaps that cause friction in practice: approval wording is narrower than real usage, Feedback and Conclusion sections lack structure, the post-feedback return path is unstated, the Approach queue's origin is unspecified, and `active.md`'s format is loose. Two minor inconsistencies exist around map callouts and the map-edit engagement rule. Tighten the wording so the process document matches how it's actually used and is unambiguous for a fresh agent.

## Approach

### 1. Approval wording

Broaden the whitelist and guard against affirmatives that carry new questions.

`PROCESS.md:69` becomes:

> **Approval** — only valid when the user gives a clear affirmative in direct response to the agent asking — e.g. "approved", "yes", "y", "ok", "go ahead", "sounds good". Silence, ambiguity, or tangential replies are not approval; neither is a message that raises new questions or concerns.

### 2. Feedback and Conclusion section structure

Give each section a minimal shape so they stay consistent across changes.

**Feedback** (written during build when something needs attention; may coexist with Conclusion if the build still completed):

> - **Status:** implemented / partially implemented / not implemented
> - **Notes:** what came up, what's unclear, and — for partial or not implemented — what the planner should reconsider
> - **Documentation impact:** any project documents that may need review (e.g. map, spec, README)

**Conclusion** (written when all tasks are done; required to complete the change):

> Comment only on anything new — deviations, docs touched, or surprises not already captured. If nothing new, "Completed." suffices.

This aligns with the existing gate at `PROCESS.md:59-60`: "implemented" → Conclusion written → build done; "partially/not implemented" → no Conclusion → replanning.

### 3. Post-feedback return path

Make the return path explicit: the user decides which stage to resume at.

Add near `PROCESS.md:12`:

> When a change returns to plan mode, the user decides whether to re-open the Approach or revise only the Plan. The Feedback section's Notes should surface enough detail for that decision.

### 4. Approach queue origin and purpose

Clarify that Pending/Current is a conversational device, not document structure, and say how the queue is seeded. Keep `changes/agents/` portable — no outward references — but inline a short "why" so the rationale survives in isolation.

Replace `PROCESS.md:29-38` with:

> Discuss one topic per message. In each message, show a **Pending** queue and the **Current** topic so the user sees how much is still unaddressed. The queue is a conversational device, not part of the change document — the Approach section records resolved outcomes.
>
> **Pending**
> 1. topic B
> 2. topic C
>
> **Current**
> What should we do about topic A?
>
> The agent drafts the initial topic list from reading the code and (if present) the map, and shows it before starting. Topics may be added, reordered, or dropped as discussion proceeds. Wait for the user's response before moving on.
>
> The grain size matters: many small decisions with the user's full attention, rather than one overwhelming list. Fine-grained negotiation belongs in planning — not building.

### 5. `active.md` format

Pin the content to just the filename. Stage and progress are derivable from the change document itself, so adding them here would create a second source of truth.

Replace `PROCESS.md:49`:

> On Plan approval, create `changes/open/active.md` containing the filename of the change (e.g. `tighten-agent-instructions.md`, with no path prefix). This is the lock — only one change builds at a time. If `active.md` already exists, stop and tell the user. An agent resuming an interrupted build reads the change document itself to find the next unticked task.

### 6. Collapse map callouts to a single kind

Replace the four callout kinds (`DECISION`, `ASSUMPTION`, `CONSTRAINT`, `TODO`) with one: `[!IMPORTANT]`. Audit of `/root/deck/map.md` showed CONSTRAINT and TODO unused, and the DECISION/ASSUMPTION distinction adding classification overhead without payoff — the prose already carries the semantic load (words like "assume", "decided", "never block").

Update `MAP-GUIDANCE.md`:
- Replace the four-kind list with `[!IMPORTANT]` as the single callout.
- Update the node-format example accordingly.
- Tighten the "when to use it" guidance: reserve for load-bearing points where skimming would lose the reader — design trade-offs, non-obvious assumptions, constraints that shape the whole node. Not for every notable fact.

Downstream effect on the deck project: the existing `/root/deck/map.md` has 5 callouts to rewrite against the new stricter bar, and the deck project's copy of `changes/agents/` needs to be refreshed from this one. Leave a draft proposal in `/root/deck/changes/open/` for the deck planner to pick up — this project's change does not touch deck's code directly.

### 7. Map-edit engagement rule caveat in README

The README's "Exempt from the active change requirement" list (`README.md:21`) names map editing as exempt, but omits the engagement rule from MAP-GUIDANCE.md. A fresh agent reading only the exemption could miss the "only with user engagement, one node at a time" constraint.

Replace the `README.md:21` bullet with:

> - Editing `map.md` — permitted without an active change, but only with user engagement (never silently, one node at a time). See MAP-GUIDANCE.md for the full rules.

## Plan

- [x] Update `changes/agents/PROCESS.md:69` — broaden Approval wording per Topic 1.
- [x] Update `changes/agents/PROCESS.md:55-64` — add Feedback and Conclusion templates per Topic 2.
- [x] Update `changes/agents/PROCESS.md:12` — add post-feedback return path sentence per Topic 3.
- [x] Update `changes/agents/PROCESS.md:29-38` — reword Approach queue section per Topic 4 (conversational device, seed + evolve, inline rationale).
- [x] Update `changes/agents/PROCESS.md:49` — tighten `active.md` format per Topic 5.
- [x] Update `changes/agents/MAP-GUIDANCE.md` — collapse callouts to a single `[!IMPORTANT]`, update the node-format example, tighten the when-to-use guidance per Topic 6.
- [x] Update `changes/agents/README.md:21` — add engagement caveat to map-edit exemption per Topic 7.
- [x] Create `/root/deck/changes/open/map-callout-consolidation.md` — intent-only draft proposal for deck's planner, covering: (a) audit the 5 existing callouts against the new stricter `[!IMPORTANT]` bar, (b) refresh deck's copy of `changes/agents/` from this project.
- [x] Re-read `README.md`, `PROCESS.md`, and `MAP-GUIDANCE.md` end-to-end after all edits, checking for consistency, orphan references, and coherent flow. Found and fixed one orphan reference: `README.md:12` said "review map impact" but the new Feedback template broadens this to "documentation impact" (map, spec, README).

## Feedback

- **Status:** implemented
- **Notes:** The Plan named `changes/agents/*` as the edit targets, but those files are generated copies — the authoritative source is `/root/cod/agent/*`, and `opt-in.py` overwrites the copies on any opt-in run. Edits have now been replayed against the authoritative files; both trees are byte-identical. The root cause of the confusion is that cod's own `CLAUDE.md` points at `@changes/agents/README.md`, which creates a circular reading loop: an agent working on cod learns the process from the generated copies and has no signal that they're generated.
- **Documentation impact:** Follow-up guidance is warranted to prevent this recurring — options discussed with user: (a) repoint cod's `CLAUDE.md` to `agent/README.md` directly, and/or (b) have `opt-in.py` prepend a "generated — do not edit" banner to each copied file. Not yet scheduled as a change.

## Conclusion

Completed. Two edits beyond the original Plan: `README.md:12` state-scan label updated from "review map impact" to "review documentation impact" to align with the broadened Feedback template; and the full set of edits was replayed against the authoritative source in `/root/cod/agent/` after the copy-vs-source confusion was caught. Downstream action lives in `/root/deck/changes/open/map-callout-consolidation.md` for the deck planner to drive.
