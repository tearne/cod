# Rename Joy principle to Flow

## Intent

The **Joy** principle in `PRINCIPLES.md` uses emotional language that may not land well across the developer community — for some it risks reading as soft or performative. **Flow** captures the same protected state (engaged, dialogic, not passive review) using vocabulary developers already carry (Csikszentmihalyi flow state), at a more neutral emotional register.

Rename the principle and update all downstream references consistently, without changing its substance.

## Approach

All references to Joy live in `agent/PRINCIPLES.md` (no other file mentions it). Three touchpoints — the Goal list item, the principle section itself, and the artifact-economy corollary sentence — all need wording adjustments so "flow" reads naturally in place of "joy / joyful". Proposed final text for each:

### Goal #2

> **Structural thinking must sustain flow.** The part of software development that strong practitioners value most — holding a system's shape in your head, deciding where the next change goes, seeing how pieces fit — is the same activity that builds comprehension. A process that turns the user into a passive reviewer destroys engagement even if it delivers correct software. Flow is a binding constraint, not a pleasant side-effect.

### `### Flow` principle section

> ### Flow
>
> The activities the map invites — integrating new concepts into the model, verifying coherence between parts, hunting edge cases, engaging in dialogue about structure — are the ones that sustain flow. They are creative, critical, and dialogic. None are "review the agent's diff." A process that delivers comprehension through passive review still fails — engagement collapses when the work becomes a maintenance burden rather than the part the user got into the field for.
>
> A corollary: **artifact economy.** Every word in a change document, Approach, or map node competes with the reader's attention. Bloat and duplication turn a dialogic activity into a wading exercise — the same engagement collapse described above, by another route. Concision and avoiding duplication are therefore not style preferences but disciplines that protect flow.

### Changelog

At Conclusion time, add a dated entry noting the rename.

## Unresolved

Parked for further thought before advancing. The proposed rename preserves the substance (dialogic/creative/critical activity, "the part the user got into the field for", artifact economy) but softens three things:

- **Rhetorical punch lost.** "Joy is a binding constraint" was memorable partly because it was a little shocking. "Flow is a binding constraint" is flatter.
- **Aspiration dimmed.** Joy was aspirational (actively cultivate). Flow is more conditional (don't break the state). Operationally clearer, slightly less ambitious.
- **Csikszentmihalyi drift.** A reader who knows flow-state technically (challenge-skill balance, immediate feedback, loss of self-consciousness) may expect the section to match that framework. It doesn't — we're really talking about dialogic engagement, not flow state in the strict sense.

### Alternative words to consider

- **Joy** — keep it; accept the palatability risk. Strongest emotional register and the sharpest "binding constraint" line.
- **Flow** — current proposal. Developer-native vocabulary but carries Csikszentmihalyi baggage and loses aspiration.
- **Engagement** — neutral and operational; matches the existing "engagement collapses" language. Low rhetorical punch.
- **Craft** — dignifies the activity; aspirational without being emotional. "Structural thinking must remain craft" is awkward, though.
- **Immersion** — absorption without Csikszentmihalyi baggage. Slightly passive feel.
- **Agency** — captures the active/dialogic point directly; passive review removes agency. Narrower than Joy covered.
