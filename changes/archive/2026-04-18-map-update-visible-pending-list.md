# Visible pending list for map updates

## Intent

When a map update touches multiple nodes, the agent should keep a visible list of the pending nodes and work through them one at a time, so the user sees what is ahead — not just the node currently under discussion. This restores, for map maintenance specifically, the "see what's coming" quality of the old topic-queue mechanic that was retired from the Approach stage. `MAP-GUIDANCE.md` and `PRINCIPLES.md` are the natural homes for the rule.

## Approach

### The mechanic

When a map edit will touch more than one node, the agent enumerates the affected nodes up front — a short visible list — and then works through them per the Engagement rule (one at a time, negotiated). As each node is settled, the agent marks it done in the list. The user sees what's coming, not just the node currently under discussion.

### When it applies

- **Spontaneous multi-node edits** (outside a change) — the user flags a restructure affecting several nodes; the agent enumerates, confirms the list is right, then works through them.
- **Stale-map catch-ups touching multiple nodes** — noticed mid-Approach or otherwise; same pattern.
- **Change-driven map edits** already satisfy this: the per-node subsections in the Approach are themselves the visible list. No additional mechanic needed — this rule is what happens when the edits aren't pre-staged in an Approach.

### Where the list lives

Chat, stated up front before any per-node work begins. The list is ephemeral — it exists to give the user the "see what's coming" view during the editing session and doesn't need a persistent home. Progress through it is visible by the agent ticking or removing entries as it goes.

### Document updates required

- `agent/MAP-GUIDANCE.md` — add the mechanic under "How the rules play out," as a short addition covering multi-node spontaneous and catch-up edits. Change-driven edits are already covered by the per-node Approach layout.

`PRINCIPLES.md` does not need an update. The original note suggested it as a candidate, but the mechanic is implementation-level — belongs with the other engagement mechanics in `MAP-GUIDANCE.md`, not with the principles explaining *why* the approach works.

## Plan

- [x] Update `agent/MAP-GUIDANCE.md` "How the rules play out" section — add a short note that when a spontaneous or catch-up edit touches two or more nodes, the agent enumerates the affected nodes in chat up front and ticks through them as each is settled. Change-driven edits (pre-staged in the Approach) already satisfy this and need no extra mechanic.

## Feedback

- **Status:** implemented
- **Notes:** Build extended beyond the original single plan task. Reviewing the result in context, the surrounding "When to edit the map" section read as verbose — the new multi-node rule landed on top of derivation-as-prose rather than clean directives. Applied a mid-build tightening with user approval: cut the "How the rules play out" section, folded the multi-node enumeration rule onto the Engagement rule where it naturally belongs, and trimmed redundant re-explanations. No directive was dropped; only the connective prose that narrated them.
- **Documentation impact:** `agent/MAP-GUIDANCE.md` "When to edit the map" section rewritten beyond the original plan.

## Conclusion

Completed, with the above Feedback covering the mid-build scope extension.
