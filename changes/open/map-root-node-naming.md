# Map root node naming

## Intent

Agents are often unsure what to name the root node of a new map. There's no guidance in `MAP-GUIDANCE.md` and no default convention, so the result is ad-hoc.

The `Deck` project's map uses `Application` as the root — generic and safe, but bland. Using the project name (`Deck`) as the root would be natural, except it clashes when a component inside the system shares the name (Deck has a `Deck` node for the mixing surface itself, which would then collide with the root).

Decide on a convention for root node naming that works across projects and handles the name-collision case, and capture it in `MAP-GUIDANCE.md` so agents don't have to invent one each time.
