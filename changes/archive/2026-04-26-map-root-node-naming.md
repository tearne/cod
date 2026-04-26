# Map root node naming

## Intent

Agents are often unsure what to name the root node of a new map. There's no guidance in `MAP-GUIDANCE.md` and no default convention, so the result is ad-hoc.

The `Deck` project's map uses `Application` as the root — generic and safe, but bland. Using the project name (`Deck`) as the root would be natural, except it clashes when a component inside the system shares the name (Deck has a `Deck` node for the mixing surface itself, which would then collide with the root).

Decide on a convention for root node naming that works across projects and handles the name-collision case, and capture it in `MAP-GUIDANCE.md` so agents don't have to invent one each time.

## Approach

### Convention: file-root H1 names its subtree, unambiguously

The H1 of any file in a map names what that file's subtree is. The root of `map.md` names the whole project; the root of a split-out subtree file names that subtree.

Default to the project's name at the top-level root — it orients the reader and names what the children belong to.

The governing rule is unambiguity: every file-root H1 must have a unique heading across the entire map, because duplicate headings break navigation — different tools handle the clash differently (markdown renderers append fragile `-1` anchors; editor jump-pickers show indistinguishable choices), and all of them make links unreliable. When the project name clashes with a prominent internal concept, style is a taste call — examples in the guidance text below.

### Guidance text for `MAP-GUIDANCE.md`

Add a subsection at the end of `## Structure: a tree of nodes`, titled `### Root node naming`:

> ### Root node naming
>
> Default to the project's name at the root. Every file-root H1 must be unambiguous with every other heading in the map — duplicates break navigation (fragile auto-generated anchors, indistinguishable jump-picker entries).
>
> When the project name clashes with a prominent internal concept, pick whichever form reads best:
>
> - Domain scoping term for the root ("Audio Player", "Build Tool").
> - Suffix ("Deck Application Map", "Deck Map Subtree").
> - Parenthetical ("Deck (Application)").
> - Rename the internal node more specifically.
>
> Prefer a term that carries domain information over a generic "Application".

## Plan

- [x] Add a `### Root node naming` subsection at the end of `## Structure: a tree of nodes` in `agent/MAP-GUIDANCE.md`, matching the guidance text above.

## Conclusion

Completed as planned.

Changelog entry added under `## 2026-04-26`.
