# Review map-edit rules for consistency

## Intent

The rules for when the map may or may not be edited now live across several places — `MAP-GUIDANCE.md`, `PROCESS.md`, `README.md`, and recent archived change documents — and have accumulated enough that a real contradiction slipped through: the just-landed "during a change, read, never edited" rule conflicts with both the existing "the map can be updated at any time" permission and the spontaneous-edit path we explicitly said covers stale-map cases noticed during Approach.

This change is a consistency pass. Survey every project file that says something about when map edits are allowed, surface the rules they collectively express, and check whether they describe a coherent model. Reconcile contradictory phrasing where possible; where the accumulated ruleset is genuinely too complex, propose a simpler model rather than patching.

The concern is complexity as much as correctness — if the rules are too many or too subtly conditional to hold in mind, something will drift again.

## Approach

### What the ruleset says today

Statements about when the map may be edited, across the live files:

- `README.md` L31: "Editing `map.md` — permitted without an active change, but only with user engagement (never silently, one node at a time)."
- `MAP-GUIDANCE.md` L103: "The map is exempt from the active change requirement — it can be updated at any time."
- `MAP-GUIDANCE.md` L105: "Only with user engagement. Never update the map silently or in bulk. Discuss each structural change with the user, and only update one node at a time."
- `MAP-GUIDANCE.md` L106: "During a change: the map is **read, never edited** in Intent and Approach ... Required map edits are laid out in the Approach and executed as Plan tasks during Build."
- `MAP-GUIDANCE.md` L114: "Outside a change: the user may want to restructure the map spontaneously. Support this."
- `PROCESS.md` L29 (Approach): "read it to understand the affected area ... but do not edit it. Map edits are deferred to Build."
- `PROCESS.md` L41 (Plan): "Map update tasks sit alongside implementation tasks."
- `PRINCIPLES.md` L85-91: "one node at a time" for "map maintenance"; scoped away from "Approach-stage negotiation."
- Archived `2026-04-18-defer-map-updates-past-planning.md`: stale-map catch-ups during Approach route via the spontaneous-edit path.

### The contradiction

"The map can be updated at any time" (L103) and "read, never edited during Intent and Approach" (L106, L29) are directly opposed. The archived change's stale-catch-up carve-out sits outside both. The rules are phrased around **lifecycle stage** when the real distinction is about **what the edit represents**.

### The simpler model

Two orthogonal rules, each small enough to hold in mind.

**Sync rule** — *The map describes what exists, not what is proposed.* Do not edit the map to describe work that is still pending. Edits that would put the map ahead of the code are deferred until the code is built.

**Engagement rule** — *Every map edit is negotiated.* One node at a time, with user engagement. Never silent, never bulk.

From these two, every lifecycle behaviour we currently spell out falls out as a derivation:

- A change requiring map updates pre-negotiates them in the Approach (per-node, full proposed content — the mechanic we just landed) and executes them as Plan tasks during Build, after the code they describe has been produced. Sync rule satisfied; engagement rule satisfied by the Approach-time per-node negotiation.
- A stale map noticed during Approach can be caught up on the spot. The edit describes existing code, so the sync rule permits it; the engagement rule still applies.
- Pure spontaneous restructuring outside any change: same as above — describes existing reality, negotiated per-node.

No lifecycle-keyed absolutes. No "read-only during Intent and Approach" rule that has to be reopened for catch-ups. The change process sits under the sync rule as the mechanism for handling the common case of proposed-not-yet-existing map updates.

### Document updates required

- `agent/MAP-GUIDANCE.md` — rewrite "When to edit the map" around the two rules, with the change-process interaction as a derivation. Keep the per-node Approach-layout subsection; move it into the new structure.
- `agent/PROCESS.md` — the Approach section currently says "do not edit it" absolutely. Narrow it to "do not edit the map to describe the proposed change" (stale catch-ups remain allowed). Likely a pointer to `MAP-GUIDANCE.md` is enough.
- `agent/README.md` — L31 bullet says "permitted without an active change." Reconcile with the sync rule: the permission is really "edits that describe existing reality."
- `agent/PRINCIPLES.md` — replace the "Interaction grain size for map maintenance" section with:

  > ### Interaction grain size for map edits
  >
  > The agent must never advance the map's structure faster than the user can engage with it. Every map edit is negotiated one node at a time — the agent proposes, the user decides.
  >
  > Without this, the user's role becomes approving map diffs instead of code diffs: a better level of abstraction, but still passive review. Per-node negotiation is what converts map maintenance into comprehension-building, which is the whole point.
  >
  > The rule holds for every kind of map edit. When a change pre-stages map edits in its Approach, per-node negotiation happens there; Build executes the pre-decided edits without reopening the question.

## Plan

- [x] Rewrite `agent/MAP-GUIDANCE.md` "When to edit the map" section around the Sync rule and Engagement rule. State each rule directly, then derive the change-process behaviour (pre-staged per-node edits in Approach, executed in Build) and the catch-up / spontaneous paths as consequences. Preserve the per-node Approach-layout subsection (full proposed node content for updates; removal/move handling; global-renames subsection).
- [x] Update `agent/PROCESS.md` Approach section: narrow "do not edit it" to "do not edit the map to describe the proposed change" — stale catch-ups remain permitted. Keep the pointer to `MAP-GUIDANCE.md`.
- [x] Update `agent/README.md` L31 bullet: reframe the map-editing exemption so it reads as "edits that describe existing reality are permitted without an active change," consistent with the Sync rule.
- [x] Replace `agent/PRINCIPLES.md` "Interaction grain size for map maintenance" section with the agreed rewrite captured in the Approach.

## Conclusion

Completed.
