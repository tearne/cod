# Guidance for Writing Maps

Working principles for building conceptual maps of software systems. Emerging from practice — expect these to evolve.


## Structure: a tree of nodes

A map is a tree. Each node is a `#` heading followed by navigation links, prose, and optional sections. The tree structure is encoded in the links, not in the filesystem or heading hierarchy.

A rendered tree overview at the top of the map file aids orientation — keep it in sync with the nodes below. Use box-drawing characters in a fenced code block:

```
Application
├ Deck
│ ├ Waveform Colour
│ ├ Detail Waveform
│ │ ├ Wide Buffer
│ │ └ Sliding Viewport
│ └ Transport
├ Browser (TODO)
└ Settings (TODO)
```

Mark unmapped nodes with `(TODO)`. Place the tree at the end of the root node, after its prose.

### Node format

```markdown
# Node Name

[Up](#parent)
[Down](#child-one)
[Down](#child-two)

Terse conceptual description. Lead with the mental picture.

> [!IMPORTANT] callout for a load-bearing point the reader should not skim.

**Detail**

Implementation-level precision — parameters, thresholds, protocols.
The user can stop reading before this; the agent reads through it.

**See also**

- [Other Node](#other-node) — why the relationship matters
```

### Navigation links

Each node carries markdown links encoding its position in the tree:

- `[Up](#parent)` — one link to the parent. Omitted only for the root node.
- `[Down](#child)` — one link per child.
- Links are standard markdown anchors, navigable with `gd` in editors with a markdown LSP (marksman recommended).
- To see a node's siblings, go Up — the parent's Down list shows them all.

### Who maintains what

- **The user maintains the content** — prose, decisions, assumptions, and conceptual relationships (what is a child of what).
- **The agent maintains the navigation links** and flags inconsistencies.

### Node sections

All optional. Always in this order when present:

- **Prose** — terse conceptual description, leads with the mental picture. This is what the user reads.
- **Callouts** — `[!IMPORTANT]` for load-bearing points where skimming would lose the reader: design trade-offs, non-obvious assumptions, constraints that shape the whole node. The prose carries the semantic load (words like "assume", "decided", "never"); the callout just marks "don't skim this". Not for every notable fact.
- **Detail** — implementation-level precision (parameters, thresholds, algorithms). The user can stop reading before this. Marked with bold `**Detail**`.
- **See also** — cross-cutting references that aren't parent/child. Marked with bold `**See also**`. Each entry says why the relationship matters.

### Root node naming

Default to the project's name at the root. Every file-root H1 must be unambiguous with every other heading in the map — duplicates break navigation (fragile auto-generated anchors, indistinguishable jump-picker entries).

When the project name clashes with a prominent internal concept, pick whichever form reads best:

- Domain scoping term for the root ("Audio Player", "Build Tool").
- Suffix ("Deck Application Map", "Deck Map Subtree").
- Parenthetical ("Deck (Application)").
- Rename the internal node more specifically.

Prefer a term that carries domain information over a generic "Application".


## Node sizing

Aim for under ~800 characters per node. The real test: if a node feels like it warrants sub-sections, it's too big — split into children. Flag nodes that exceed this to the user.


## The only-child preference

Prefer folding a singleton child into its parent. Keep it as its own node when it is a distinct concept in the user's model, or when its detail would bloat the parent. A useful test: if a sibling were later added, would this still be a node? If yes, keep it now.


## Content principles

- Lead with the mental picture, not the implementation.
- Name the boxes before explaining them ("three mechanisms: A, B, C" — then a node each).
- Not code-structure-coupled — may discuss technical concepts when load-bearing, but should not mirror module structure, reference function names, or break on refactor.
- Use continuous lines (no hard wraps mid-sentence) for soft-wrap compatibility.
- Blank line between bullet points for readability.


## File organisation

The format is agnostic about how nodes are distributed across files:

- **Single file** — all nodes in one file, linked by anchors. Good for smaller systems.
- **Multiple files** — nodes spread across files, linked by relative paths. Good for larger systems.
- Navigation links work identically either way — `[Up](#parent)` for same-file, `[Up](other-file.md#parent)` for cross-file.


## When to edit the map

Two rules govern every map edit.

**Sync rule** — *The map describes what exists, not what is proposed.* Don't edit the map ahead of the code. Edits that describe pending work defer until the code is built.

**Engagement rule** — *Every map edit is negotiated.* One node at a time, with user engagement. Never silent, never bulk. When an edit touches two or more nodes, enumerate them in chat up front and tick through them as each is settled. Per-node approval prompts are phrased as comprehension checks — "does that fit your mental model?", "is that clear enough?" — not yes/no gates.

The map is exempt from the active-change requirement: edits that describe existing reality may happen at any time.

### Map edits and the change lifecycle

Map edits are negotiated per-node per the Engagement rule — never pre-staged as wholesale node bodies in an Approach. Map-only work happens as per-node negotiation directly, exempt from the change lifecycle alongside the existing active-change exemption.

For code changes, Approach and Plan typically don't propose map edits and Build doesn't touch the map. Map catch-up follows the build as a per-node negotiation. The completed change's Conclusion may carry a starter draft. Tightly-bound exceptions where small map work rides along a code change are allowed when it genuinely fits.


## Maintaining the map

Signals that the map needs attention:

- **A node feels like it needs sub-sections** — split into children.
- **Top-level boxes don't match the user's mental model** — restructure. The map follows the user's model, not the code's architecture.
- **A node has grown verbose** — cut aggressively. Move precision to **Detail**.
- **New concepts don't have a natural home** — the decomposition may need rethinking, not a misc section.
- **An only-child exists that isn't a distinct concept** — fold it into its parent.

Don't treat the map as append-only. Restructuring is not rework — it's what keeps the map useful.

**Ambiguity test.** Regularly ask whether each node in the affected area is sufficiently well characterised that a fresh agent could build from it without guessing. Flag ambiguities to the user — they are map quality issues, not implementation issues.
