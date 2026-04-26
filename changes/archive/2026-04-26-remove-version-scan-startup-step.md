# Remove the version-scan startup step

## Intent

Delete step 2 of `agent/README.md`'s "On startup" list. It tells the agent to scan `changes/agent/` for sibling versioned directories and flag migration concerns on every startup, but there's no signal of which version was previously active, so the comparison has no anchor. Replace it with a brief on-update section: when the user reports an update, the agent looks at the new version's installed `CHANGELOG.md` and the previous version (recoverable from `CLAUDE.md`'s `@` pointer history) and surfaces anything migration-relevant. Reactive instead of every-session, and short enough that the agent has the layout it needs without groping.

## Approach

### Delete step 2

Remove the second numbered item from the "On startup" list in `agent/README.md`. Renumber the remaining items (steps 3 and 4 become 2 and 3).

### Add a short "On version update" section

A brief section between "On startup" and "Rules" describing the on-update behavior. The agent only reads the installed `agent/README.md` (which becomes `changes/agent/<version>/README.md` in a consumer), so the layout has to be told there or the agent has to discover it on the fly. Proposed wording:

> ## On version update
>
> When the user reports the agent directory has been updated, identify the new and previous versions from `CLAUDE.md`'s `@` pointer — current value and prior value from git history. Read the new version's `CHANGELOG.md` (each version directory ships its own) for the entries between then and now, and surface migration concerns.

Self-contained, no-ops in the cod source repo (which has no `changes/agent/` and never receives the signal).

### Scope is contained

Only one "framework" reference exists across the agent docs (verified by grep), and it's the sentence being deleted. No further references to "step 2" exist in the codebase, so renumbering is purely cosmetic. No sweep needed.

### Rename the change document

Filename `generalise-framework-startup-scan.md` no longer matches the change. Rename to `remove-version-scan-startup-step.md` as a Plan task.

## Plan

- [x] Delete step 2 from the "On startup" list in `agent/README.md`; renumber the remaining items (3→2, 4→3).
- [x] Insert a new `## On version update` section in `agent/README.md`, between "On startup" and "Rules", with the wording agreed in the Approach.
- [x] Rename `changes/open/generalise-framework-startup-scan.md` to `changes/open/remove-version-scan-startup-step.md` (and update `changes/open/active.md` to match).

## Log

- The renumbered step 3 (formerly step 4) used to read "Report the scan results, any additional version directories, and propose next steps". Dropped the "any additional version directories" clause because nothing scans for them anymore — the Plan said "renumber", but leaving that phrase in would have referred to a deleted concept.

## Conclusion

Completed. The Log records the only deviation worth noting (renumbered step 3 lost its trailing clause about additional version directories).
