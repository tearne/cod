# Change modes

**Mode:** Formal

## Intent

Make the shape of a change an upfront, named choice rather than something buried in plan-stage options. Three modes:

- **Formal** — the current full sequence: Intent → Approach → Plan-as-tasks → Build → Conclusion. The default; the agent uses it unless told otherwise.
- **Explore** — same gates as Formal, but the Plan is topics + done-when rather than a task checklist. For work where depth and coverage matter more than a fixed step list. Today this exists as a buried sub-option of the Plan stage and appears to be underused; promoting it to a named mode is partly about discoverability.
- **Wander** — Intent only, then straight to Build, with the Conclusion written retrospectively to capture the final approach. The change name may be updated to reflect where it ended up. The agent may periodically remind the user the change is in Wander mode, and offer to "flush" (conclude/archive) when the user appears to be moving on. Discarded Wander changes are fine; keeping a record of them may also be useful.

Mode is chosen per change and can be changed mid-flight — a change can be paused and rewritten into a different mode if the work turns out to want a different shape.

Origin: hub75 process-feedback (2026-05-03) sketching an "agile mode" after a session where that cadence ran naturally; broadened here to cover the full set of shapes the framework already half-supports.

## Approach

### Mode chosen after Intent

Intent first; the agent then proposes a mode (default Formal) and the user confirms. Before Intent there isn't enough shape to choose.

### Mode recorded in the change document

A `**Mode:** <name>` line directly under the title.

### What each mode runs

- **Formal** — Intent → Approach → Plan-as-tasks → Build → Conclusion.
- **Explore** — same as Formal, Plan as topics + done-when.
- **Wander** — Intent → Build, retrospective Conclusion. No Approach, no Plan. Takes the `active.md` lock on entering Build like the others.

### Mid-flight mode change

User-initiated: pause, rewrite the change document into the target mode's shape, resume.

### Wander upkeep

The agent reminds the user a Wander change is open when it detects a topic shift, and may offer to flush. Discarded Wander changes are just deleted — no archive record.

### Guidance lands in PROCESS.md

A new "Modes" subsection at the top of Plan mode names the three modes and points at the existing Approach/Plan/Build sections.

## Plan

- [x] Add Modes subsection at the top of `PROCESS.md` Plan mode introducing Formal, Explore, Wander.
- [x] Tie Plan-shape options (tasks vs topics) to Formal vs Explore in the Plan stage description.
- [x] Add Wander procedure to `PROCESS.md`: Intent → Build, retrospective Conclusion, topic-shift flush prompts, delete-on-discard.
- [x] Add mid-flight mode-change rule to `PROCESS.md`.
- [x] Add Mode line (`**Mode:** <name>` under title) to the change-document conventions.
- [x] Update startup scan states in `agent/README.md` to cover Wander shapes.
- [x] Bump version (date-based, kind: minor — new framework feature). → 2026-05-04.1

## Log

- Added Wander-specific note to Completing section: Conclusion is retrospective and captures the approach; change name updated if work ended elsewhere. Wasn't an explicit Plan task but follows directly from Wander's "no Approach" structure.
- Added a one-line "(Formal and Explore only — Wander skips this stage.)" header to the Approach section so readers landing there directly know the constraint.
- Pre-existing contradiction spotted between line 10 (active stays if code changed) and line 103 (remove active.md on blocker). Resolved both conditional: blocker removes `active.md` only when no code has been changed; half-finished builds stay active. Adjacent fix done in this change.

## Conclusion

Completed. Beyond the planned work, the change resolved a pre-existing contradiction between the Modes section and the Executing section about when `active.md` is removed on a blocker. No map impact (this repo has no `map.md`).

Proposed changelog entry (2026-05-04.1):

> `PROCESS.md`: change documents now declare a **Mode** under the title. **Formal** is the existing full sequence. **Explore** swaps the Plan checklist for topics + done-when. **Wander** runs Intent → Build → retrospective Conclusion with no Approach or Plan, gets topic-shift flush prompts, and is deleted (not archived) on discard. Mode is chosen after Intent (default Formal) and can be changed mid-flight by rewriting the document. Adjacent fix: blocker handling keeps `active.md` when code has been changed.
