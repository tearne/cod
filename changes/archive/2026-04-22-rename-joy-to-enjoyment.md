# Rename Joy principle to Enjoyment

## Intent

The **Joy** principle in `PRINCIPLES.md` uses emotional language that may not land well across the developer community — for some it risks reading as soft or performative. **Enjoyment** preserves the positive affect but dials the register down one notch, without taking on technical baggage (as **Flow** would, via Csikszentmihalyi's flow state).

Rename the principle and update all downstream references consistently, without changing its substance.

## Approach

All references to Joy live in `agent/PRINCIPLES.md` (no other file mentions it). Three touchpoints — the Goal list item, the principle section itself, and the artifact-economy corollary sentence — need the one-word swap.

### Goal #2

> **Structural thinking must remain enjoyable.** The part of software development that strong practitioners value most — holding a system's shape in your head, deciding where the next change goes, seeing how pieces fit — is the same activity that builds comprehension. A process that turns the user into a passive reviewer destroys engagement even if it delivers correct software. Enjoyment is a binding constraint, not a pleasant side-effect.

### `### Enjoyment` principle section

> ### Enjoyment
>
> Enjoyable activities using the map include integrating new concepts into the model, verifying coherence between parts, hunting edge cases, and engaging in dialogue about structure. These are creative, critical, and dialogic. None are "review the agent's diff." A process that delivers comprehension through passive review still fails — engagement collapses when the work becomes a maintenance burden rather than the part the user got into the field for.
>
> A corollary: **artifact economy.** Every word in a change document, Approach, or map node competes with the reader's attention. Bloat and duplication turn a dialogic activity into a wading exercise — the same engagement collapse described above, by another route. Concision and avoiding duplication are therefore not style preferences but disciplines that protect enjoyment.

### Changelog

At Conclusion time, add a one-line entry noting the rename.

## Plan

- [x] Update Goal #2 in `agent/PRINCIPLES.md` to the wording above ("joyful" → "enjoyable"; "Joy" → "Enjoyment" in the trailing sentence).
- [x] Rename `### Joy` to `### Enjoyment` and update the section body per the wording above ("Joyful" → "Enjoyable").
- [x] Update the artifact-economy corollary: "protect joy" → "protect enjoyment".
- [x] At Conclusion: add a changelog entry describing the rename.

## Conclusion

Completed.
