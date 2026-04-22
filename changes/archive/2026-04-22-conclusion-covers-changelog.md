# Conclusion covers version/changelog

## Intent

At the end of every change, the Conclusion section should be used to consider whether a version bump or changelog update is warranted. Currently `PROCESS.md` has a separate "Changelog entry" step after Completing; this proposal suggests the consideration belongs inside the Conclusion itself — so the act of writing the Conclusion naturally prompts the question, rather than it being a separable post-step.

## Approach

### Fold the changelog step into the Conclusion definition

The Conclusion is already the reflect-on-what-just-happened moment; adding changelog worthiness to its list of duties is natural and removes a separately-headed step. The mechanics (how to write the entry, `.N` rule, version source-of-truth note) stay attached to the Completing section but no longer need their own subsection.

### Broaden "review" to "review and/or test"

If the change produces something runnable, the user may want to test it, not just read the diff. Say so explicitly in the Completing flow.

### Add project-side versioning as a Completing duty

If the project under change uses its own versioning scheme, advance the last digit before handing a build to the user for test, so the user can visually confirm they're on the latest. Announce the new value. This is a visibility guarantee, not a judgement call — the bump happens routinely, not only for "substantive" changes. Separate from `agent/CHANGELOG.md`, which versions the COD framework itself. Kept conditional on the project having its own versioning.

### Proposed `### Completing` section

> ### Completing
>
> When all tasks are done, write a Conclusion section. Ask the user to review and/or test. On approval, move the change file to `changes/archive/` (prefixed `YYYY-MM-DD-<name>.md`), remove `active.md`.
>
> **Conclusion** covers:
>
> - Anything new — deviations, docs touched, or surprises not already captured in the change document. If nothing new, "Completed." suffices.
> - Whether the change warrants an entry in `agent/CHANGELOG.md`. Trivial edits (typo fixes, minor doc wording) may not; for anything substantive, draft a one-line entry and surface it in chat for approval or reword.
> - If the project under change uses its own versioning scheme, advance the last digit before handing the build to the user for test, so they can visually confirm they're on the latest. Announce the new value.
>
> On approval of the changelog entry, add a new `## YYYY-MM-DD[.N]` section at the top of `agent/CHANGELOG.md` with the entry beneath. `.N` increments when today already has a section. The version name is the source of truth for the next `opt-in.py` install — the changelog heading becomes the target's directory name.

The existing `### Changelog entry` subsection is removed — its content is absorbed into the above.

### Changelog

At Conclusion time, consider whether a one-line entry is warranted for this structural tweak to the Completing flow.

## Plan

- [x] Update `agent/PROCESS.md` `### Completing` section to match the proposed text in the Approach.
- [x] Remove the `### Changelog entry` subsection from `agent/PROCESS.md`.
- [x] At Conclusion time: consider changelog entry per the new rule.

## Conclusion

Mid-build, the project-versioning rule was relocated from a Conclusion bullet to a short paragraph at the top of `## Build mode` — the rule applies to any hand-over during iteration, not only at Completing. Also reworded to reference `ADDITIONAL/VERSIONING.md` rather than inline semver mechanics. Patched in place (not via Feedback → replan), on user instruction.

Separately, the user flagged that project changelog headings should follow the project's versioning scheme, and that the COD framework itself should dogfood this by moving `agent/CHANGELOG.md` to semver. Captured as a new proposal after archive.
