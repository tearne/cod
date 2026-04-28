# Keywords

## Process keyword

At any point in a session the user may start a message with `process:` to capture an observation about the agent or the change process itself.

On a `process:` message, the agent:

- Appends a dated entry to `changes/process-feedback.md`, creating the file with a `# Process feedback` header if it doesn't yet exist. The entry is the observation plus whatever context (mode, active change, preceding topic, relevant file) would be lost otherwise. It need not be verbatim; the agent may tighten or rephrase to make the entry readable on its own later.
- Confirms capture in a single line.
- Returns to whatever task was under way without acting on the observation.

`changes/process-feedback.md` is a single append-only file, tracked in git, shared between collaborators.


## Aside keyword

At any point in a session the user may use `aside:` (most naturally at the start of a message; other natural forms are also recognised) to park a topic for later without breaking the current flow.

On an aside, the agent:

- Dispatches the topic. **New proposal** (a fresh `changes/open/<slug>.md` with the captured text as Intent) if the topic is independent of the current discussion or no active discussion exists. **In-proposal aside** (appended to an "Asides" subsection at the end of the current change document) if the topic is within the scope of an in-progress change. The agent decides based on scope; when genuinely unsure, asks.
- Acknowledges placement in a single line ("Captured as new proposal: …" or "Added to asides in current change: …").
- Returns to whatever task was under way.

In-proposal asides during Intent/Approach/Plan discussion fold into the change as planning proceeds. In-proposal asides during Build sit until Conclusion time, when the user decides their fate (fold into Conclusion, spin off as new proposals, or discard).
