# Conversation stack management

## Intent

The user should be able to park a topic mid-conversation with the keyword **"aside"**. When said, the agent captures the item for discussion later — either as a draft proposal in `changes/open/` or held in a visible stack of things to come back to — without breaking the current flow.

This is a specific instance of a broader need: some form of conversation stack management. The agent needs a consistent way to hold pending topics that arise while the user's attention is committed elsewhere, surface them at the right time, and discharge them as they're addressed.

## Approach

### Trigger

The user uses "aside" to park a topic — most naturally `aside:` at the start of a message (paralleling `process:`), but the agent recognises other natural forms ("Aside — ...", or a sentence-initial "aside" followed by the topic). The agent captures the parked topic, dispatches it per the rule below, acknowledges in one line, and returns to the flow under way.

### Dispatch rule

An aside has two possible homes:

- **New proposal** — an independent topic warranting its own change. The agent creates `changes/open/<slug>.md` with the captured text as Intent (same behaviour as `take a note`).
- **Discussion point in the current change** — the topic is within the scope of an in-progress discussion. The agent adds the item to an "Asides" subsection at the end of the current change document, for the user to fold in as the discussion progresses.

The agent decides based on scope: an aside that clearly belongs to the change under discussion goes in-place; an aside with no obvious home becomes a new proposal. When genuinely unsure, ask. Otherwise, place the aside, inform the user in one line ("Captured as new proposal: …" or "Added to asides in current change: …"), and continue.

### When there is no active discussion

All asides become new proposals. The dispatch question only arises when there's an in-progress change to attach to.

### Surfacing and discharging

- **New-proposal asides** surface through the startup scan of `changes/open/`.
- **In-proposal asides during Intent/Approach/Plan discussion** surface when the user next reads the current change document, to be folded into the Approach (or resolved otherwise) as part of normal planning.
- **In-proposal asides during Build** sit in the Asides subsection until Conclusion time. When the build completes, the user reviews any accumulated asides and decides their fate: fold into the Conclusion, spin off as new proposals, or discard. They are distinct from Feedback (which the agent writes when the plan itself turned out wrong) — asides are user-parked thoughts that don't block execution.

No separate tracking file or visible stack — items live where they'll be acted on, which is enough.

### Document updates required

- `agent/PROCESS.md` — add an "Aside keyword" subsection at the end, parallel to "Process feedback". Describe the trigger, the dispatch rule (new proposal vs. in-proposal subsection), the no-active-discussion default, and the one-line acknowledgement.

## Plan

- [x] Add an "Aside keyword" subsection to `agent/PROCESS.md` at the end, parallel to "Process feedback". Describe: the trigger (`aside:` most naturally, other natural forms also recognised); the dispatch rule (new proposal in `changes/open/` vs. an "Asides" subsection in the current change doc when in-scope); that with no active discussion all asides become new proposals; that in-proposal asides during Build sit until Conclusion time, distinct from Feedback. Include the one-line acknowledgement rule.

## Conclusion

Completed.
