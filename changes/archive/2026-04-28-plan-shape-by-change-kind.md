# Plan shape should fit the change kind

## Intent

`PROCESS.md`'s Plan stage assumes a checklist of discrete tasks (add, update, remove, test). For exploratory changes that doesn't fit — the rigid task list makes the agent push toward "ship it" cadence when the user wants to go deep. Surfaced during cardplayer's `memory-deep-dive`, where the agent kept reaching for a checklist Plan before the shape settled.

## Approach

### Plan shape carries the cadence

The Plan takes whatever shape fits the work; the shape itself signals the cadence, so no separate "kind" label is needed. Mirrors the planner/builder split for map work: planner negotiates, builder executes.

`PROCESS.md` introduces two Plan building blocks the planner combines as the work demands:

- **Tasks.** Discrete checklist items, each ticked as completed. Used for incremental, definite work.
- **Topics + done-when.** A list of topics to cover plus a "done when…" condition. No tick boxes. Used for exploration.

Both can sit in one Plan when a change calls for it. Each block gets a short rendering template and brief picking guidance.

### Builder follows what's written

`PROCESS.md`'s Executing rule relaxes from "tick each task" to "follow the Plan". Ticks apply where there are tasks; topics are worked toward the done-when condition. A Plan with both blocks combines the two cadences. The existing "stop if the plan is wrong" rule already covers Builder-side struggles, so no new exit-and-replan mechanism is needed.

## Plan

- [x] Add the two Plan building blocks (Tasks; Topics + done-when) to `PROCESS.md`'s Plan stage, with a short rendering template for each and brief picking guidance.
- [x] Relax `PROCESS.md`'s Executing rule from "tick each task" to "follow the Plan" — ticks apply where tasks are present; topics are worked toward the done-when condition.
- [x] Bump version (date-based: next entry, resolved at Build start). → `2026-04-28.1`

## Log

- Plan stage's old line "Map update tasks sit alongside implementation tasks — same list, same execution" contradicted the per-node-map-edits rule (code-change Plans typically don't propose map edits). Dropped as part of the Plan-stage rewrite.

## Conclusion

Completed. Log records the stale map line dropped from the Plan stage as part of the rewrite.

### Proposed changelog entry

```
## 2026-04-28.1

- `PROCESS.md`: Plan stage now offers two building blocks — Tasks (the existing checklist) and Topics + done-when (for exploration) — that combine as the work demands. Executing rule relaxes to "follow the Plan", ticking where tasks are present and working topics toward the done-when condition. The Plan's shape itself signals the cadence; no separate "kind" label introduced. Also dropped a stale map line that contradicted the per-node-map-edits rule.
```
