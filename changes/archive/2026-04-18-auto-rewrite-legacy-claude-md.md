# Auto-rewrite legacy `CLAUDE.md` pointer

## Intent

When opt-in is run on a project that had previously opted in under the old layout, its `CLAUDE.md` still contains the pre-unification pointer `@changes/agents/README.md`. The current script detects this situation but only prints a cleanup instruction; the file itself is left untouched. Opt-in should overwrite `CLAUDE.md` to the new pointer `@agent/README.md` automatically — but only when safe: the project must be a git repository and the file must have no uncommitted changes, so the rewrite can always be undone with `git restore`.

## Approach

**Rewrite conditions.** The rewrite is considered only when `CLAUDE.md` contains the exact known-legacy content `@changes/agents/README.md\n` — no fuzzy matching. Given that content, the decision splits on git state:

- **Tracked and unmodified** → overwrite. Restorable with `git restore`.
- **Tracked and modified** → refuse. The user has local edits that must not be clobbered.
- **Untracked (including gitignored)** → overwrite, but do not stage. The file's tracking state is the user's concern; opt-in only rewrites content.

**Integration point.** A dedicated helper `rewrite_legacy_claude_md(project_root)` runs before the existing `create_file` call for `CLAUDE.md`. It encapsulates the git-state probe, the exact-content match, and the rewrite. Keeping it separate from `create_file` preserves `create_file`'s narrow responsibility and makes the legacy logic easy to remove once it's no longer needed.

**Warning text adjustments.** `warn_if_legacy_layout` receives the rewrite outcome and tailors the CLAUDE.md step: omit it when the rewrite succeeded, keep a short "left untouched — …" note when refused. A stale cleanup step would erode the warning's signal.

## Plan

- [x] Add `rewrite_legacy_claude_md(project_root)` to `agent/opt-in.py`. Returns one of `"rewrote"`, `"refused"` (with reason), or `"inapplicable"`. Checks for exact legacy content `@changes/agents/README.md\n`, inspects git state (tracked + unmodified / tracked + modified / untracked), and overwrites only when safe. Reports its action via `report()`.
- [x] Call `rewrite_legacy_claude_md` from `main()` immediately before the existing `create_file` call for `CLAUDE.md`, capturing the return value.
- [x] Update `warn_if_legacy_layout` to accept the rewrite outcome and adjust the printed CLAUDE.md step: omit when the rewrite succeeded, keep a short "left untouched — …" line when refused.
- [x] Test: in a scratch `git init` directory with `CLAUDE.md` containing `@changes/agents/README.md`, run opt-in and confirm the file is rewritten and the warning omits the CLAUDE.md step.

## Conclusion

Completed. Verified three paths in scratch repos: **rewrote** (untracked legacy file auto-updated), **inapplicable** (customised content left alone, warning omits CLAUDE.md step), **refused_modified** (tracked-and-dirty legacy file preserved, warning keeps the step with a reason note).

One minor surprise: when the helper successfully rewrites, the subsequent `create_file` call still runs and reports "already present" for `CLAUDE.md`. Correct behaviour but slightly noisy — worth watching if output tidiness becomes a concern later.

