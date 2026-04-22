# Only-child rule exceptions

## Intent

The only-child rule in `MAP-GUIDANCE.md` says: "If a node would have no siblings and no children, it's not a node — it's the bottom of its parent." The rule pushes against accidental nesting, but it also gets in the way of cases where a concept is genuinely a distinct sub-concept of its parent and benefits from its own node — even when it happens to have no siblings (yet or ever).

Rework the rule so it holds its structural intent (don't wrap a bullet in a node for no reason) without blocking logically-nested singleton concepts that deserve separate framing.

## Approach

### Reframe the rule as a preference, not a mandate

Rewrite the `## The only-child rule` section in `MAP-GUIDANCE.md` so it expresses a preference with an explicit escape clause, rather than a hard "it's not a node" ruling.

Proposed wording:

> **The only-child preference.** Prefer folding a singleton child into its parent. Keep it as its own node when it is a distinct concept in the user's model, or when its detail would bloat the parent. A useful test: if a sibling were later added, would this still be a node? If yes, keep it now.

Reason: the original mandate catches pointless wrapping but overreaches when a legitimately nested concept happens to have no siblings. The escape clause preserves the anti-pattern guard while allowing singleton sub-concepts that carry their own identity.

### Update the maintenance-signals list to match

The "Maintaining the map" section lists "An only-child exists — fold it into its parent" as a signal. Change to: "An only-child exists that isn't a distinct concept — fold it into its parent." Keeps the signal useful without contradicting the new preference framing.

### Changelog

At Conclusion time, add a `## 2026-04-22.1` entry noting the rule relaxation.

## Plan

- [x] Rewrite the `## The only-child rule` section in `agent/MAP-GUIDANCE.md` as a preference with an escape clause, including the "if a sibling were added, would this still be a node?" test
- [x] Update the "An only-child exists" bullet in the "Maintaining the map" signals list to match the new preference framing
- [x] At Conclusion time: draft changelog entry, prompt the user, add a `## 2026-04-22.1` section to `agent/CHANGELOG.md`

## Conclusion

Completed.

