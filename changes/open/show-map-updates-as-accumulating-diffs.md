# Show map updates as accumulating diffs within full node context

## Intent

When proposing updates to a node's text in the map, the agent should show the changes as diffs within the full node context, rather than just the changed segments in isolation. Presenting the whole node each time lets the user see changes accumulate across a discussion and judge whether the node still reads well as a whole. The user then decides when to "flush" the accumulated changes to the file by approving — a bit like committing to file.
