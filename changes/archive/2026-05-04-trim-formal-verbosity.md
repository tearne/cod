# Trim formal verbosity

## Intent

Formal change documents have been running too long. The length itself generates resistance — the user feels friction picking up a formal change because there is so much to read. The existing guidance ("state the decision, then the reason in a sentence or two. Stop.") isn't biting; the agent's default verbosity wins.

Push the framework toward shorter, denser change documents — Approach and Plan in particular — without losing the load-bearing "why" that makes formal worth the ceremony. Doing this before the change-modes work lets us dogfood the trimmer formal mode while writing the modes change itself.

## Approach

### Self-prune pass before surfacing

After drafting Approach (and Plan), the agent re-reads its own draft and removes anything that doesn't carry a decision-and-reason: recap of Intent, file-by-file rehearsal, hedging, restating choices already in proposed map nodes. The agent only surfaces the post-prune version.

### Every line justifies itself

The per-line rule is the quality gate: each line either carries a decision-and-reason or comes out. The prune pass enforces it.

### Length-triggered condense request

If the post-prune Approach still exceeds 1000 characters, the agent asks the user whether to condense further and highlights borderline content — significant material that might get cut but isn't essential — so the user can adjudicate. Characters inside tables and diagrams are exempt from the count.

### Plan prune rules

- One task per atomic outcome.
- No "why" — Approach's job.
- No obvious sub-steps.
- No ceremony tasks ("review", "double-check") without a real gate.
- Don't restate file paths the task name already implies.

### Scope

Approach and Plan only. Intent and Conclusion are already constrained.

## Plan

- [x] Add self-prune step and 1000-char condense trigger to `PROCESS.md` Approach section.
- [x] Add Plan prune rules to `PROCESS.md` Plan section.
- [x] Bump version (date-based, kind: patch-equivalent — guidance refinement). → 2026-05-04
- [x] Re-read `PROCESS.md` end-to-end against the new prune rules and surface candidate cuts to the user.

## Log

- Review pass: surfaced 6 candidate cuts; user actioned 4 directly (old lines 12, 17, 47, 74), agent then made 4 further compressions (stage-draft repetition, log-hedging, Feedback-restatement at end of Executing, changelog-prose).

## Conclusion

Completed. The dogfooding pass produced more shrinkage than the planned additions cost — `PROCESS.md` is net shorter, and the new prune rules visibly bite.

Proposed changelog entry (2026-05-04):

> `PROCESS.md`: Approach gains a mandatory self-prune step before surfacing — every line must carry a decision-and-reason — and a 1000-character condense trigger that asks the user to adjudicate borderline content if exceeded (tables and diagrams exempt). Plan gains a short list of prune rules (one atomic outcome per task, no "why", no obvious sub-steps, no ceremony tasks, no redundant file paths). Several existing paragraphs across Plan mode and Build mode trimmed in the same pass.
