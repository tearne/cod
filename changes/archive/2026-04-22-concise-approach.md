# More concise Approach sections

## Intent

Agents produce reasonably concise Intent sections, but the Approach tends to sprawl — long prose, over-explanation, restating the Intent, spelling out details that belong in the Plan or that the reader can infer. The result is harder to review and hides the load-bearing decisions in noise.

Tighten the guidance in `PROCESS.md` so agents treat the Approach as a set of decisions and their reasons, not a narrative. The reader should be able to scan the Approach and see what's being decided without wading through recap or implementation trivia.

## Approach

### Reframe the Approach as decisions, not narrative

Rewrite the opening paragraph of the `### Approach` subsection in `PROCESS.md` so that the framing leads with what the Approach *is* (a list of decisions with short reasons) rather than what it *contains* ("the full Approach"). The word "full" currently licenses sprawl.

### Add a short "What it is / isn't" list

Immediately after the opening paragraph, add a short bulleted list making the expected shape concrete:

- One subsection per decision; self-evident choices don't need a subsection.
- State the decision, then the reason in a sentence or two. Stop.
- Don't recap the Intent. Don't rehearse code structure or file-by-file steps — those belong in the Plan.
- If a subsection can be deleted without losing a decision, delete it.

### Leave the Unresolved and Plan mechanics alone

The surrounding text about the Unresolved list, disclosure in chat, and the transition to Plan is already tight and doesn't need rewording. The change is scoped to the opening frame plus the new list.

### Changelog

At Conclusion time, add a `## 2026-04-22` section to `agent/CHANGELOG.md` noting the Approach tightening.

## Plan

- [x] Rewrite the opening paragraph of `### Approach` in `agent/PROCESS.md` to frame the Approach as decisions-and-reasons rather than "the full Approach"
- [x] Add the "What it is / isn't" bulleted list immediately after the opening paragraph
- [x] At Conclusion time: draft the changelog entry, prompt the user, add a `## 2026-04-22` section to `agent/CHANGELOG.md`

## Conclusion

Completed.

