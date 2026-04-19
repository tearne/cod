# Map update as a comprehension checkpoint

## Intent

The moment the agent seeks approval on a map edit is a natural comprehension checkpoint, but "approve?" frames it as a yes/no gate rather than a probe. A small wording change carries the intent: phrase map-edit approval requests as "does that fit your mental model?" or "is that clear enough?" — same gating effect, but the phrasing signals that the user should check their understanding of the node, not just rubber-stamp the edit. This avoids adding a heavyweight mechanic while still reclaiming the map-update moment as a comprehension checkpoint instead of a mechanical transcription of what just shipped.

## Approach

### The mechanic

When the agent seeks user approval for a proposed map node edit, phrase the request in terms of comprehension rather than acceptance. Examples:

- "Does that fit your mental model?"
- "Is that clear enough?"
- "Does the node read well as a whole?"

The prompt still functions as a gate — affirmative proceeds, negative opens discussion — but the wording asks the user to check their understanding of the node, not merely rubber-stamp the proposed text.

### When it applies

- **Per-node approval during spontaneous or catch-up edits.**
- **Per-node negotiation during a change's Approach** — when discussing each node's proposed content in the pre-staged subsections, the comprehension-check wording applies.

Full Plan approval is unaffected: that gate covers many tasks at once and isn't a per-node comprehension moment.

### Document updates required

- `agent/MAP-GUIDANCE.md` — add a short clause to the Engagement rule indicating that per-node approval requests use comprehension-probing phrasing, with one or two example phrasings.

## Plan

- [x] Update `agent/MAP-GUIDANCE.md` — add a short clause to the Engagement rule: when asking for approval on a proposed per-node edit, phrase the prompt as a comprehension check ("does that fit your mental model?", "is that clear enough?"), not a yes/no approval. Full Plan approval is unaffected.

## Conclusion

Completed.
