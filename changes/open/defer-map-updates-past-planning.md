# Defer map updates past the planning stage

## Intent

Modifying the map during the planning stage feels wrong. If the plan is not immediately approved and we don't proceed with the change, the map ends up reflecting a state that was never built — out of sync with the code. The map should be updated at a point in the change process where the work the map describes has actually happened (or is committed to happening), not while the plan is still a draft.
