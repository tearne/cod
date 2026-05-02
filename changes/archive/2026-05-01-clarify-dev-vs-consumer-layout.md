# Clarify dev-vs-consumer layout difference

## Intent

This repo authors a framework that consumers receive via `opt-in.py`. The two layouts differ, and nothing here flags that — so bugs that only break consumer projects (a framework file silently missing from opt-in's copy list) can stay hidden because the dev repo loads everything directly and never notices.

`KEYWORDS.md` is currently in this state: `agent/README.md` `@`-imports it, but `opt-in.py`'s `FRAMEWORK_FILES` doesn't include it, so consumers don't receive it and its `@`-import fails silently. `PRINCIPLES.md` is a related but inverse case — it sits inside `agent/` but is never `@`-imported anywhere, and no consumer-side documentation references it; copying it to consumers would just produce an orphan file.

Make the dev-vs-consumer difference visible up front in the agent README so future sessions are primed to check `opt-in.py` early when reasoning about what consumers see, fix the missing `KEYWORDS.md` copy, and reposition `PRINCIPLES.md` as dev-repo reference material at the project root rather than agent-context content.

## Approach

### Priming lives in the project root README, loaded into agent context

The note has two requirements: visible to dev agents, absent from consumer copies. `agent/README.md` is copied verbatim by `opt-in.py`, so a note added there reaches consumers — wrong context for them. The top-level `README.md` is the natural home for "what this project is" framing; adding `@README.md` to this repo's `CLAUDE.md` (alongside the existing `@agent/README.md`) loads it into agent context. This repo's `CLAUDE.md` is exempt from `opt-in.py`'s pointer-rewrite logic since the script refuses to run here, so the deviation from the canonical single-pointer pattern is fine.

Within the top-level README, the note sits as its own section after `Contents` — a reader has the file layout in mind before meeting the framing shift, and the existing `Contents` and `Changelog` sections stay focused on their own concerns.

### Fix `FRAMEWORK_FILES` and reposition `PRINCIPLES.md`

`KEYWORDS.md` is added to `opt-in.py`'s `FRAMEWORK_FILES` list, since `agent/README.md` `@`-imports it and consumers were missing it. `PRINCIPLES.md` moves out of `agent/` to the project root: it's reference material for users evaluating the framework, doesn't belong in agent context (would clutter every session) and doesn't belong in consumer projects (no agent path loads it; no human pointer to it on the consumer side). The dev-repo top-level `README.md` already cites it, and root placement makes that pointer one directory shorter.

## Plan

**Version bump:** new dated release (date-based equivalent of minor — distinct concern, not a same-day `.N` refinement of an earlier change).

- [x] Add `KEYWORDS.md` to `FRAMEWORK_FILES` in `opt-in.py`.
- [x] Move `agent/PRINCIPLES.md` to the project root and update the top-level `README.md` link.
- [x] Add `@README.md` to this repo's `CLAUDE.md`, alongside the existing `@agent/README.md`.
- [x] Add a new section to the top-level `README.md`, between `Contents` and `Changelog`, naming the dev-vs-consumer layout difference and pointing at `opt-in.py` as the source of truth for what consumers see.
- [x] Add a new dated CHANGELOG.md entry describing the priming, the `KEYWORDS.md` copy fix, and the `PRINCIPLES.md` move.

## Log

- Mid-build review (user-requested) found that `PRINCIPLES.md` was never `@`-imported by `agent/README.md`, so the original Plan's "add `PRINCIPLES.md` to `FRAMEWORK_FILES`" task would have shipped it as an orphan — present but unloaded and undiscoverable in consumer projects. After discussing four resolutions, the user chose to move `PRINCIPLES.md` out of `agent/` to the project root, treating it as dev-repo evaluator reference material. Intent, Approach, Plan, and CHANGELOG entry all updated to reflect the new direction.

## Conclusion

Shipped as `2026-05-01`; bump kind unchanged from Plan. Mid-build pivot captured in the Log; CHANGELOG entry was a planned task and already covers the priming, the `KEYWORDS.md` copy fix, and the `PRINCIPLES.md` relocation.


