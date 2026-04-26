# Per-node map edits

## Intent

`MAP-GUIDANCE.md`'s pre-staging convention treats wholesale commit of full node bodies as the default for any map work in a change. That collides with the per-node, comprehension-check negotiation the rest of the framework calls for — Build degenerates to "execute this exact text" rather than the interactive step `MAP-GUIDANCE.md` itself describes. Surfaced during cardplayer's `m4a-support`, where the user found pre-staging too coarse for map work.

## Approach

### Map edits are per-node, never pre-staged

The Engagement rule governs all map edits. The "Pre-staging edits in an Approach" convention (wholesale commit of node bodies) drops. Map-only work happens as per-node negotiation directly, exempt from the change lifecycle alongside the existing active-change exemption.

### Code changes: map work picked up afterwards

For code changes, Approach and Plan typically don't propose map edits and Build doesn't touch the map. Map catch-up follows the build as a per-node negotiation. Conclusion may carry a starter draft. Tightly-bound exceptions where small map work rides along a code change stay allowed.

### Standing post-build review

When handing a finished build back for user review, the planner flags whether the map needs catching up. Sits in `PROCESS.md`'s Completing section.

## Log

- During review, the user pushed back on the map-only branch (Build applies negotiated text). Collapsed to: map work is exempt from the change lifecycle entirely (sits alongside the existing active-change exemption). Also softened "Build doesn't touch the map" — kept as the typical case but with the door open for rare tightly-bound exceptions. MAP-GUIDANCE, PROCESS, and the Approach in this doc updated in place.

## Conclusion

Completed. The Log records the in-review Approach revisions; nothing further worth noting.

### Proposed changelog entry

```
## 2026-04-26.2

- `MAP-GUIDANCE.md` and `PROCESS.md`: removed pre-staging of map edits in an Approach. Map-only work happens as plan-mode per-node negotiation, exempt from the change lifecycle. For code changes, Build typically doesn't touch the map; map catch-up follows the build as a per-node negotiation, with rare tightly-bound exceptions still allowed. The Completing section now prompts the planner to flag whether the map needs catching up at hand-back time.
```

## Plan

- [x] Replace `MAP-GUIDANCE.md`'s "Pre-staging edits in an Approach" subsection with the per-node rule, including the map-only carve-out (Build applies negotiated text).
- [x] Update `PROCESS.md`'s Approach stage to drop the pre-staging cross-reference and state that code changes don't propose map edits.
- [x] Add the standing post-build map review to `PROCESS.md`'s Completing section.
- [x] Rename the change file to `per-node-map-edits.md` and update `changes/open/active.md` to match.
