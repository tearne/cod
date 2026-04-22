# Avoid duplication between Approach prose and map node updates

## Intent

When a change pre-stages map edits, the proposed full node content already expresses what's changing. The Approach prose often restates the same thing in different words, producing unnecessary duplication: the reader gets the decision twice, once as narrative and once as the new node.

Adjust the guidance so that when a decision is fully carried by a proposed node update, the Approach text doesn't repeat it. The per-node subsection *is* the decision. Prose in the Approach should be reserved for decisions that aren't expressed as node updates, or for the "why" that the node itself can't convey.

The aim is fewer words per change, not less information — the information lives in the node content instead of being restated above it.

## Approach

### Add the rule to the Approach "what it is / isn't" list

Add a bullet to the list in `PROCESS.md` under `### Approach`: "When a decision is fully carried by a proposed map node update, don't restate it in prose — the node is the decision. Prose is for decisions that aren't in a node, or for 'why' the node can't convey."

Reason: the anti-duplication rule belongs alongside the other Approach-writing discipline agents already read. MAP-GUIDANCE.md stays focused on node mechanics; PROCESS.md owns Approach style.

### Extend the Joy principle with artifact economy

Add a short paragraph to the `### Joy` section of `PRINCIPLES.md`:

> A corollary: **artifact economy.** Every word in a change document, Approach, or map node competes with the reader's attention. Bloat and duplication turn a dialogic activity into a wading exercise — the same engagement collapse described above, by another route. Concision and avoiding duplication are therefore not style preferences but disciplines that protect joy.

Reason: recent tightening work (Approach concision, anti-duplication) points at the same unnamed idea. Naming it as a derivative of Joy gives future tightening decisions a principled home without inflating the principle count.

### Changelog

At Conclusion time, add a dated entry noting both the PROCESS.md bullet and the PRINCIPLES.md extension.

## Plan

- [x] Add the anti-duplication bullet to the `### Approach` "what it is / isn't" list in `agent/PROCESS.md`
- [x] Add the "artifact economy" corollary paragraph to the `### Joy` section in `agent/PRINCIPLES.md`
- [x] At Conclusion time: draft changelog entry, prompt user, add a new dated section to `agent/CHANGELOG.md`

## Conclusion

Completed.

