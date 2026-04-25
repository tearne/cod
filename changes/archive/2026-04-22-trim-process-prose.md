# Trim explanatory prose from PROCESS.md

## Intent

`PROCESS.md` has accumulated explanatory prose alongside the rules — motivation paragraphs, justifications, "why we do it this way" framings. Agents mostly need the rules to act; the reasoning is useful when judging edge cases but not when following the mainline flow.

Audit `PROCESS.md` for prose that explains *why* rather than *what to do*, and either cut it or replace it with a pointer to `PRINCIPLES.md` (which is where the reasoning already lives, or can live). The aim is a leaner PROCESS.md that reads as rules + short examples, with the principles-level reasoning reachable by link rather than inlined.

## Approach

### Cut rather than relocate

Most of the "why" prose in PROCESS.md is mechanism-specific justification — explaining why an individual rule is shaped the way it is — rather than principle-level reasoning. Moving it to PRINCIPLES.md would clutter that file with process minutiae it doesn't belong to. Straight cuts read leaner; PRINCIPLES.md pointers are reserved for the few places where a mechanism genuinely derives from a named principle and the reader needs the connection.

### Proposed cuts

Each is a short explanatory tail attached to an otherwise-operational rule. The rule keeps its operational content; only the trailing justification goes.

**`## Plan mode` intro (current line 19)** — the sentence about the user reviewing the rendered file "with the help of their editor's diff view" is justifying why chat isn't used to re-paste drafts. Cut to: "Draft goes into the change document; chat is for disclosures (notably Unresolved) and summaries, not the draft itself."

**`### Executing` (current line 64)** — trailing sentence "A well-constructed plan should not need close watching." Cut entirely.

**`### Process keyword` intro (current line 108)** — trailing sentence "These observations are raw material for later reflection — they feed back into the COD methodology when the user reviews them, not into the current task." Cut entirely; the mechanism (capture and return) already makes this clear.

**`### Process keyword` closing paragraph (current line 116)** — the disambiguation "Its name echoes the build-stage **Feedback** section... but the mechanism is distinct..." is reader-reassurance prose, not a rule. Cut the disambiguation; keep the "single append-only file, tracked in git, shared between collaborators" fact as it's operational.

**`### Aside keyword` closing sentence (current line 129)** — the disambiguation "They are distinct from `Feedback` — Feedback is agent-written... asides are user-parked thoughts..." Cut; parallel to the process-keyword disambiguation above.

### Keep

Audited and deliberately retained:

- `## Modes` line 12 tail about Feedback Notes — operational guidance for the replanning gate.
- `### Entering build` "This is the lock — only one change builds at a time." — concise and load-bearing for understanding `active.md`.
- `### Approach` line 45 "its absence signals that the Approach is settled." — tiny operational cue.

## Plan

- [x] `agent/PROCESS.md` `## Plan mode` intro: replace the "user reviews the rendered file..." sentence with "Draft goes into the change document; chat is for disclosures (notably Unresolved) and summaries, not the draft itself."
- [x] `agent/PROCESS.md` `### Executing`: remove the trailing sentence "A well-constructed plan should not need close watching."
- [x] `agent/PROCESS.md` `### Process keyword` intro: remove the trailing sentence about observations being "raw material for later reflection..."
- [x] `agent/PROCESS.md` `### Process keyword` closing paragraph: remove the disambiguation prose ("Its name echoes... mechanism is distinct..."); keep the append-only/tracked/shared fact.
- [x] `agent/PROCESS.md` `### Aside keyword` closing paragraph: remove the disambiguation prose distinguishing asides from Feedback.
- [x] At Conclusion: consider changelog entry.

## Conclusion

Completed.
