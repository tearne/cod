# Comprehension Oriented Design (COD)

## The problem

In traditional software development, building a system and understanding its structure were not two activities — they were one. The mental model was a free byproduct of the keystrokes required to produce the code. You could not write the system without simultaneously building the conceptual model.

Agent-augmented development broke this bundle. Agents accelerated production dramatically and accelerated comprehension by approximately zero. Because production used to carry comprehension along with it, removing the user from production didn't just slow comprehension — it removed the mechanism by which structural understanding was acquired.

The symptom is familiar: specifications grow until unread. The user asks the agent instead. But agent answers are query-on-demand — they answer the immediate question but leave no durable structural residue. No model accumulates. The user is always behind the system (reactive querying) instead of ahead of it (designing, planning). This manifests as unexpected side-effects when changes touch connections the user didn't know existed.

Two strategies have been observed to fail:

1. **Richer specifications** — specs grow until they are not read. Agents can summarise on demand, but query-on-demand answers don't build structural understanding.

2. **More legible code** — lowers the per-line cost of reading, but doesn't change the fact that comprehension is now a separate, unbudgeted activity on an ever-growing surface.

The problem is not an artefact problem but an activity problem: the activity that used to produce the model has been removed from the user's loop, and no artifact can substitute for the activity itself.


## The approach

COD replaces the lost comprehension-building activity with a new one: maintaining a navigable map of the system. The map is a tree of concepts — structured around how the user naturally thinks about the system, not how the code is organised. Agents render the map into code. The user's job is to maintain the map; the agent's job is to ensure the map has sufficient specificity for faithful rendering, and to handle implementation complexity that doesn't belong in the user's model.

The map is also the natural level for structural reasoning. Logic bugs — wrong flows, missing cases, incorrect boundaries — live at the structural level but are obscured at the code level by syntax, error handling, and language idioms. Working at the map makes them visible before any code is written.


## Goal

A way of working in which both users and agents can shine on software projects, subject to three binding constraints:

1. **Comprehension must scale with complexity.** The user's structural grip on the system must not decay as the system grows.

2. **Structural thinking must remain enjoyable.** The part of software development that strong practitioners value most — holding a system's shape in your head, deciding where the next change goes, seeing how pieces fit — is the same activity that builds comprehension. A process that turns the user into a passive reviewer destroys engagement even if it delivers correct software. Enjoyment is a binding constraint, not a pleasant side-effect.

3. **Conceptual maintainability is a first-class design constraint.** It has the same standing as correctness and performance. It is not the first thing sacrificed under deadline pressure.


## Principles


### Comprehension is an activity

No artifact substitutes for the activity of structural thinking itself. The process must give the user a deliberate activity that builds and maintains structural understanding at a pace that keeps up with agent-driven production. The map is that activity — maintaining it is the construction that builds the conceptual model.


### Enjoyment

Enjoyable activities using the map include integrating new concepts into the model, verifying coherence between parts, hunting edge cases, and engaging in dialogue about structure. These are creative, critical, and dialogic. None are "review the agent's diff." A process that delivers comprehension through passive review still fails — engagement collapses when the work becomes a maintenance burden rather than the part the user got into the field for.

A corollary: **artifact economy.** Every word in a change document, Approach, or map node competes with the reader's attention. Bloat and duplication turn a dialogic activity into a wading exercise — the same engagement collapse described above, by another route. Concision and avoiding duplication are therefore not style preferences but disciplines that protect enjoyment.


### Local sufficiency

The goal of the map's structure is local sufficiency: the property that reasoning about one part of the system does not require holding the rest in mind. This is what makes a system feel manageable — the mind registering that working memory is sufficient for the task.

Cross-cutting concerns are the enemy of local sufficiency. When the same fact has consequences in many places, no local mental model is ever sufficient. The solution is to promote each cross-cutting concern to a first-class named object, referenced locally and visually, rather than letting it accumulate as an implicit horizontal dependency. Everything a reader needs to understand a node should be visible near that node.


### Trees over graphs

The map aims to be a tree, not a DAG or a graph. Trees give local sufficiency for free — every node has one parent, one home, one context. Real domains have cross-cutting relationships, but these are handled as references between tree nodes, not as additional parent-child edges. The tree is the primary structure; cross-references are decoration on it. Similarly, complex internal behaviour — cycles, fan-out, retry loops — lives inside a node, not between nodes. The tree describes how concepts relate to each other; what happens inside a concept can be arbitrarily complex.

The "peak tree" — the stage where a system's structure feels like a clean logical tree — is a real cognitive state, and its loss is the felt experience of complexity becoming unmanageable. Agent-driven development is uniquely dangerous to this: agents will produce graph-shaped code from day one, skipping the entire portion of the lifecycle where the work felt good. The map preserves the peak-tree experience indefinitely.


### Conceptual maintainability

Conceptual maintainability — can a user still hold, reason about, and evolve the system's model? — has the same standing as correctness and performance. This follows a progression in language and paradigm design:

- **Type systems** made type correctness structural.
- **Functional programming** made local reasoning about functions safe.
- **Ownership and borrow checking** made memory safety structural.

Each step took a property that humans valued but could not sustain by discipline alone, and turned it into a structural guarantee enforced by a mechanism. COD follows the same pattern at whole-system scope: the property being guaranteed is that the conceptual model remains cognitively maintainable as the system grows. The enforcement mechanism is the agent — a flexible translator that renders a cognitively clean model into whatever the implementation requires.

Building a model of a real system is always a negotiation between domain fidelity, practical constraints, and cognitive manageability. The third term — historically the first sacrificed — must now have equal standing, because without the construction-comprehension bundle there is no fallback to recover understanding.


### Cross-agent falsifiability

If the map is the source of truth, multiple agents can render it independently. Differences between renderings are a built-in test of the map's quality. A good map renders consistently; a bad one doesn't. This answers two otherwise difficult questions. How does the user catch abstraction leaks without reading code? — leaks show up as cross-agent disagreement. How does the user detect drift between their model and reality? — drift appears when re-rendering produces different code without an explaining map change.

Full cross-rendering is expensive and best reserved for high-stakes or low-confidence moments. The routine form is cheaper: the question "is this part of the map sufficiently well characterised that a fresh agent could build from it without guessing?" This can be asked at any time, by either user or agent, during map maintenance or planning. Another lightweight test is whether multiple agents would derive the same test conditions and edge cases from a node — divergence points to ambiguity in the map, not in the implementation. The literal cross-rendering mechanism is available when needed; the discipline of asking is the continuous quality signal.


### Interaction grain size for map edits

The agent must never advance the map's structure faster than the user can engage with it. Every map edit is negotiated one node at a time — the agent proposes, the user decides.

Without this, the user's role becomes approving map diffs instead of code diffs: a better level of abstraction, but still passive review. Per-node negotiation is what converts map maintenance into comprehension-building, which is the whole point.

The rule holds for every kind of map edit. When a change pre-stages map edits in its Approach, per-node negotiation happens there; Build executes the pre-decided edits without reopening the question.
