# Prevent Agent Source Confusion

## Intent

In the cod project, `CLAUDE.md` points at `@changes/agents/README.md`. But those files are generated copies of the authoritative `agent/*` sources, so an agent working on cod learns the process from output rather than source — and any edits it makes end up in gitignored files that `opt-in.py` overwrites. Repoint cod's `CLAUDE.md` to `@agent/README.md` so agents work on the authoritative source directly.

## Approach

### 1. Residual path reference in README

Alongside the CLAUDE.md repoint, reword `agent/README.md:41` to drop the hardcoded `changes/agents/` prefix so the description works from either source or copy location:

> - `ADDITIONAL/` — optional guides, loaded on reference. See its README for the list.

Same fix logic as the main change, applied consistently. No downstream breakage — the folder sits next to the README in both locations.

## Plan

- [x] Update `/root/cod/CLAUDE.md` — change `@changes/agents/README.md` to `@agent/README.md`.
- [x] Update `/root/cod/agent/README.md:41` — replace `changes/agents/ADDITIONAL/` with `ADDITIONAL/` per Topic 1.
- [x] Sync the same line-41 edit to `/root/cod/changes/agents/README.md:41` so the copy does not temporarily drift from its source.
- [x] Verify the new wiring by reading `/root/cod/CLAUDE.md` and confirming it resolves to the authoritative `agent/` tree (README plus its `@`-transcluded PROCESS/STYLE/MAP-GUIDANCE). Confirmed: `CLAUDE.md` contains `@agent/README.md`; `agent/` and `changes/agents/` READMEs are byte-identical; all three transcluded files present at `agent/`.

## Conclusion

Completed.
