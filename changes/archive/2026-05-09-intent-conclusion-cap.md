# Section length triggers

**Mode:** Formal

## Intent

Add 500-character triggers to Intent and Conclusion, and harmonise with the existing 1000-char Approach trigger by lifting all three into one rule with a per-section threshold table. Same mechanism throughout: over threshold, the agent flags borderlines for the user to decide rather than cutting silently. Tables and diagrams exempt.

## Approach

### One rule, table of thresholds

Lift the trigger out of the Approach section into a single `### Section length triggers` subsection under Plan mode (after Modes). The subsection states the mechanism once and lists thresholds in a table:

| Section    | Threshold |
|------------|-----------|
| Intent     | 500       |
| Approach   | 1000      |
| Conclusion | 500 (Wander: 1000) |

Plan deliberately omitted — list-shaped, prune rules already cover it.

### Mechanism wording stays as-is

Over threshold, the agent flags borderline content (significant material that might get cut but isn't essential) for the user to adjudicate. Tables and diagrams are excluded from the count. Same as today's Approach trigger; just stated once.

### Existing Approach paragraph removed

The current paragraph inside the Approach section is replaced by reference to the new subsection.

## Plan

- [x] Add `### Section length triggers` subsection (mechanism + thresholds table) under Plan mode after Modes in `PROCESS.md`.
- [x] Remove the existing 1000-char trigger paragraph from the Approach section.
- [x] Bump version (date-based, kind: patch — guidance refinement). → 2026-05-09

## Conclusion

Completed.

Proposed changelog entry (2026-05-09):

> `PROCESS.md`: section length triggers consolidated into a single rule and table under Plan mode. Intent and Conclusion gain 500-char triggers; Approach keeps its 1000; Conclusion in Wander gets 1000 (it carries the Approach work retrospectively). Tables and diagrams remain exempt. Same mechanism throughout — over threshold, the agent flags borderline content for the user to adjudicate.
