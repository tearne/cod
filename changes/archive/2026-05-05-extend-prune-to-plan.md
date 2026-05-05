# Extend prune to Plan

**Mode:** Formal

## Intent

The self-prune-before-surfacing step and the 1000-character condense trigger live only in the Approach section of `PROCESS.md`. The original trim-formal-verbosity change intended both to cover Plan as well — the wording "After drafting Approach (and Plan), the agent re-reads..." didn't make the final commit, and the threshold was scoped to Approach.

Bring Plan into scope: the self-prune step should apply to the Plan stage too, so the existing Plan prune rules have a fixed checkpoint behind them rather than relying on the agent to enforce them voluntarily.

## Approach

### Self-prune step extends to Plan

Before surfacing the Plan, the agent re-reads it and applies the Plan prune rules. Mirrors the Approach checkpoint and ties the existing rules to a fixed action rather than passive guidance.

### No length trigger for Plan

The 1000-character condense trigger stays Approach-only. Plans are checklist-shaped; verbose Plans usually mean bad task decomposition, which the prune rules already catch. A char threshold would mostly fire on legitimately long Plans for legitimately big work.

## Plan

- [x] Add a self-prune step to the Plan stage in `PROCESS.md`.
- [x] Bump version (date-based, kind: patch — guidance refinement). → 2026-05-05

## Conclusion

Completed.

Proposed changelog entry (2026-05-05):

> `PROCESS.md`: self-prune step now applies to the Plan stage as well as the Approach — agent re-reads the Plan and applies the prune rules before surfacing.
