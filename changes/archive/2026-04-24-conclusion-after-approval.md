# Write Conclusion and Feedback only after build approval

## Intent

Neither Conclusion nor Feedback should be written until the user has approved how the build is being wrapped up. Writing them earlier confuses future agents: an agent picking up the change sees a settled-looking summary already in place and cannot reconcile it with a build the user has since reopened or rejected.

During the build, a running **Log** section at the bottom of the change document captures status as it happens — surprises, partial progress, anything worth remembering. The Log may be updated at any time and is for working memory, not for the planner's consumption. When the work reaches a natural pause, the agent asks the user to review. On approval, the agent wraps the Log into either Feedback (plan needs revisiting) or Conclusion (build done), as appropriate.

The key shift: Feedback and Conclusion become agent-written summaries issued *after* alignment with the user, not signals the agent raises unilaterally. The Log carries the running state in the meantime.

## Approach

### Introduce a Log section

During build, the agent keeps a running **Log** at the bottom of the change document. Entries capture status, surprises, partial progress, and anything worth remembering between sessions. The Log is working memory — the agent may add to it at any time during build, without user prompting. Format: a bulleted list, most recent at the bottom. Each entry is one or two sentences; no required structure.

The Log is preserved into the archived change document — the archive is the complete record, so trimming the Log after writing Feedback/Conclusion would lose provenance.

### Pause-and-review replaces unilateral Feedback

The agent stops and asks the user for a wrap-up decision at two points: all plan tasks complete, or an impasse the plan can't bridge. In both cases the Log is the record the user reads; the agent highlights the key points in chat. No Feedback or Conclusion is written until the user has responded with direction.

The current rule "if the surprise is minor and the path forward is clear, continue but write a Feedback section noting what was unexpected" changes: the noting goes into the Log, not Feedback, and the agent continues. Feedback is reserved for the post-approval summary.

### Feedback and Conclusion become post-approval summaries

After the user responds to a pause-and-review, the agent writes either:

- **Feedback** — if the user agrees the plan needs revisiting. Retains the current three-part shape (Status / Notes / Documentation impact), drawn from the Log plus the user's direction.
- **Conclusion** — if the user agrees the build is done.

Both are terminal: once written, they reflect an agreed outcome and are safe for future agents to take at face value. A change document with a Conclusion is done; with Feedback (no Conclusion) is replanning.

The changelog consideration (currently a separate post-Conclusion step, and the subject of the open `conclusion-covers-changelog.md` proposal) folds into Conclusion-writing: once the user confirms the build is done, the agent drafts the Conclusion including a proposed changelog entry if warranted, surfaces it for approval, and on approval applies the changelog edit and archives. One combined approval gate, not two.

### Startup scan states

The README "On startup" list changes to reflect the new markers. Replacements:

- "Has Feedback but no Conclusion — needs replanning" — unchanged in meaning; Feedback is now always post-approval, so this state still signals replanning.
- "Has Feedback and Conclusion — build complete" — unchanged in meaning.
- "active.md exists" — still the mid-build lock, but now additionally signals "may be awaiting wrap-up decision" when all tasks are ticked. The agent reads the Log to distinguish.

A new state is needed for the impasse case: `active.md` absent, no Feedback yet, Log describes a blocker — "awaiting user direction on impasse".

### active.md on impasse

On impasse, the agent removes `active.md` to release the lock, records the blocker in the Log, and tells the user. This preserves the current behaviour of freeing the lock, with the only change being that Feedback isn't written yet.

## Plan

- [x] Update PROCESS.md mode-intro paragraphs to use pause-and-review language in place of unilateral-Feedback language
- [x] Add a **Log** subsection to PROCESS.md Build mode describing purpose, format, and preservation-on-archive
- [x] Rewrite the **Executing** subsection: minor surprises go to the Log and build continues; impasse triggers pause-and-review (release `active.md`, tell the user), not Feedback-writing
- [x] Rewrite the **Feedback** description to present it as a post-approval summary drawn from the Log and the user's direction; keep the three-part shape
- [x] Rewrite the **Completing** subsection: all-tasks-done triggers a pause-and-review rather than writing a Conclusion; on approval, agent writes the Conclusion (folding in the changelog consideration and draft), gets combined approval, applies the changelog edit, archives
- [x] Remove the standalone **Changelog entry** subsection from PROCESS.md (content absorbed into Completing)
- [x] Update the `process:` and `aside:` keyword sections' references to Feedback to reflect its new post-approval semantics
- [x] Update README.md's "On startup" state list: Log presence as a state signal, new "awaiting user direction on impasse" state, `active.md`-with-all-tasks-ticked state

## Log

- Removed redundant `conclusion-covers-changelog.md` at the start of build, per user direction. Its substance is absorbed into the Completing rewrite here.

## Conclusion

Log subsection wording was tightened during review. The initial draft described the Log as "status notes, surprises, and partial progress", which the user flagged as over-inclusive. The final text leads with "a bulleted list of the unexpected" and explicitly notes that routine execution going to plan does not need logging.

Proposed changelog entry:

```
## 2026-04-24

- `PROCESS.md`: Feedback and Conclusion become post-approval summaries, drawn from a new build-time **Log** of the unexpected. The Changelog entry step folds into Completing. `README.md` startup states refreshed to match.
```