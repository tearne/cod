# Conclusion covers version/changelog

## Intent

At the end of every change, the Conclusion section should be used to consider whether a version bump or changelog update is warranted. Currently `PROCESS.md` has a separate "Changelog entry" step after Completing; this proposal suggests the consideration belongs inside the Conclusion itself — so the act of writing the Conclusion naturally prompts the question, rather than it being a separable post-step.

## Approach

### Fold the changelog step into the Conclusion definition

The Conclusion is already the reflect-on-what-just-happened moment; adding changelog worthiness to its list of duties is natural and removes a separately-headed step. The mechanics (how to write the entry, `.N` rule, version source-of-truth note) stay attached to the Completing section but no longer need their own subsection.

### Proposed `### Completing` section

> ### Completing
>
> When all tasks are done, write a Conclusion section. Ask the user to review. On approval, move the change file to `changes/archive/` (prefixed `YYYY-MM-DD-<name>.md`), remove `active.md`.
>
> **Conclusion** covers:
>
> - Anything new — deviations, docs touched, or surprises not already captured in the change document. If nothing new, "Completed." suffices.
> - Whether the change warrants an entry in `agent/CHANGELOG.md`. Trivial edits (typo fixes, minor doc wording) may not; for anything substantive, draft a one-line entry and surface it in chat for approval or reword.
>
> On approval of the changelog entry, add a new `## YYYY-MM-DD[.N]` section at the top of `agent/CHANGELOG.md` with the entry beneath. `.N` increments when today already has a section. The version name is the source of truth for the next `opt-in.py` install — the changelog heading becomes the target's directory name.

The existing `### Changelog entry` subsection is removed — its content is absorbed into the above.

### Changelog

At Conclusion time, consider whether a one-line entry is warranted for this structural tweak to the Completing flow.
