# Defer map updates past the planning stage

## Intent

Modifying the map during the planning stage feels wrong. If the plan is not immediately approved and we don't proceed with the change, the map ends up reflecting a state that was never built — out of sync with the code. The map should be updated at a point in the change process where the work the map describes has actually happened (or is committed to happening), not while the plan is still a draft.

## Approach

### The rule

During the **Intent** and **Approach** stages, the map is **read, never edited**. The agent consults the map to understand the affected area, frame the change in domain terms, and identify coverage gaps — but does not change any node content or structural links.

All map changes required by a change become Plan tasks and execute during Build, alongside the implementation tasks. Map and code advance together, on an approved plan.

This removes a sync hazard: if the plan is revised, abandoned, or sits idle, the map is not already ahead of reality, describing an implementation that was never produced.

### How map updates appear in the Approach

When a change requires map edits, the Approach lays them out explicitly so the Plan tasks can be written directly from it:

- **Per-node edits.** One subsection per map node being changed. The subsection describes the change:
  - **Content update** — show the **full proposed node content**, not a diff. Nodes are small by design, and showing the whole node lets the user review unambiguously.
  - **Removal or move** — state what happens to the node, where its children go, and how incoming links are handled.

  Each subsection becomes its own Plan task.
- **Global renames or cross-cutting touches.** A separate subsection when a single change sweeps across many nodes in a uniform way (e.g. renaming a concept). These become cross-cutting Plan tasks rather than per-node ones.

This is how the "one node at a time, with user engagement" principle from `MAP-GUIDANCE.md` survives the shift to Build-time execution: the per-node engagement happens at Approach time, where each node's update is described and approved individually. Build then executes the pre-approved edits without renegotiating structure.

### The spontaneous-edit path is unaffected

`MAP-GUIDANCE.md` already permits map edits outside a change, with user engagement, one node at a time. This rule does not touch that path — there is no sync hazard there, because no implementation is pending.

This also absorbs the "map is stale" case. If Approach discussion reveals the map is simply behind current reality, bring it current via the spontaneous-edit path and continue. No separate change needed; the edit describes reality that already exists.

### Document updates

- `agent/MAP-GUIDANCE.md`: tighten the "During a change" bullet of "When to edit the map" to state explicitly that map reading happens in Approach, map editing happens in Build via Plan tasks — never during Intent or Approach.
- `agent/PROCESS.md`: a short clarification in the Plan mode / Approach section that map edits are deferred to Build, even when the Approach discusses the need for them.

## Plan

- [x] Update `agent/MAP-GUIDANCE.md` — rewrite the "During a change" bullet under "When to edit the map" to say: map is read-only during Intent and Approach; required map edits are laid out in the Approach using per-node subsections (full proposed node content for updates; removal/move handling for structural changes) plus an optional global-renames subsection; edits execute as Plan tasks during Build.
- [x] Update `agent/PROCESS.md` — in the Plan mode / Approach section, add a short clarification that map edits are deferred to Build via Plan tasks, even when Approach discusses them; point readers to `MAP-GUIDANCE.md` for the per-node subsection layout.

## Conclusion

Completed.
