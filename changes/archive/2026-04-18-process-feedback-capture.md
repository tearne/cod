# Capture process feedback during agent use

## Intent

While using the agent, the user often notices things about the agent's behaviour or the process itself that could be improved — but there is no structured channel for these observations. They either get addressed in the moment as instructions to the agent, or forgotten.

Introduce a concept of **feedback** during use: a lightweight way to record observations about the agent or process performance. These captures accumulate in a form that can ultimately be fed back into this project (the COD methodology), so the process refines more easily over time rather than relying on the user to remember and re-raise concerns later.

## Approach

### Capture trigger

The user starts a message with `process:` and everything following is treated as an observation about the agent or the change process, not a task to act on. The agent appends it to `changes/process.md`, confirms in one line, and returns to whatever was happening.

The word "feedback" is deliberately avoided — it already names a stage/section of the change process (build-time Feedback), and a parallel file using the same word would be confusing. `process:` was chosen despite mild overlap with `PROCESS.md`; the lowercase/uppercase distinction and the different path (`changes/process.md` vs `agent/PROCESS.md`) keep them separable in practice.

### Storage

Captured observations live in `changes/process.md` — a single append-only file, tracked in git so observations are shared between collaborators. Each entry is a dated bullet containing the observation and any context the agent adds. No categories — entries are free-form, and grouping is deferred to whoever later reads them for pattern-finding.

### Capture discipline

The agent writes each entry so it will be useful later — the user's observation plus whatever context (mode, active change, preceding topic, relevant file) would be lost otherwise. The capture does not need to be verbatim; the agent may tighten, rephrase, or re-structure to make the entry readable on its own later. The agent does not attempt to solve, rewrite, or implement the observation in the moment. One-line confirmation, then back to the task at hand.

### Scope

Observations are strictly about the agent's behaviour or the change process — not about the project's own codebase or design. The channel exists to feed back into the COD methodology; keeping scope narrow is what lets patterns emerge from the accumulated entries.

### Surfacing to COD

Observations recorded while working on any project may concern the COD methodology itself, which lives elsewhere. Cross-project syncing is not automated: when the user comes to `/root/cod` to refine the process, they review their other projects' `changes/process.md` files and bring forward observations as new notes or changes. This keeps the mechanism simple and avoids hidden cross-project dependencies.

### Opt-in integration

`opt-in.py` creates an empty `changes/process.md` (with a one-line header) so the file is present from the start of every opted-in project.

## Plan

- [x] Add a **Process feedback** section to `agent/PROCESS.md` describing the `process:` trigger, the storage file `changes/process.md`, and the capture discipline (entry is the observation plus any useful context; need not be verbatim; one-line confirmation; no in-moment action).
- [x] Update `agent/opt-in.py` to create `changes/process.md` in target projects — a one-line header such as `# Process observations` so the file exists from day one.
- [x] Seed `changes/process.md` in this source repo with the same header (the self-install guard blocks opt-in here, so this file needs to be created by hand).
- [x] Test: run opt-in in a scratch git repo and confirm `changes/process.md` is created with the header.

## Conclusion

Completed.
