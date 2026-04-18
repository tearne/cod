# Refine Approach discussion and build cadence

## Intent

Two aspects of the current change process feel overly heavy:

- **Approach discussion is verbose.** Working through a pending topic queue one item at a time generates a lot of back-and-forth text. A leaner alternative: the agent drafts the full Approach up front alongside an Unresolved list; the user scans the whole picture and the list makes it easy to see what still blocks approval.
- **Build supervision is over-watchful.** If the plan and map are well constructed, close watching during execution adds little. A review-at-end cadence — trust the plan, execute, review the completed change — should be the default.

## Approach

### New Approach-discussion mechanic

Intent remains a separately-approved gate — unchanged. What changes is how the Approach stage is conducted: the topic-queue mechanic (Pending/Current, one topic per message) is fully replaced.

Once Intent is approved, the agent reads the code, the map (if any), and relevant context, then writes the Approach section in full — resolving everything it can on its own. Alongside the Approach, the agent writes an **Unresolved** section at the end of the change document: a short bulleted list of questions the agent cannot answer alone, each pointing to the part of the Approach it affects.

After writing, the agent also discloses the Unresolved list in chat, so the user can answer immediately without opening the file.

The user reviews the draft and answers the questions (inline reply is fine). The agent folds the answers back into the Approach prose and removes resolved items from the list. When the list is empty, Approach is ready for the user's explicit approval, and the process proceeds to Plan as today. The Unresolved section is deleted once the Plan is written — it has no further purpose, and its absence signals that the Approach is settled.

If the user disagrees with something the agent had already settled, they raise it like a new item; the agent folds the resolution in, and adds new Unresolved items for any downstream choices that are now reopened.

### New build cadence

With a well-constructed plan, the build proceeds without seeking the user's attention at every step. The agent:

- Executes each plan task and ticks it in the change document as it goes.
- Posts concise on-screen updates as it works — enough for the user to see progress — but does not pause for interaction task by task.
- Only interacts mid-build when something warrants it: surprises, ambiguity, or a plan problem. Trivial progress does not.
- Still stops immediately and returns to plan mode if the plan is wrong or the path is unclear. The Feedback-without-Conclusion escape hatch is unchanged.

On completion, the user reviews the change document and the actual diffs, then approves archive as today.

### Drafting before approval

For both Approach and Plan, the agent writes the draft into the change document first, then asks for approval. The user reviews the rendered file (with their editor's diff view) rather than a chat-rendered draft. Chat is used to surface the Unresolved list and to summarise what's ready for review — not to carry the draft itself.

## Plan

- [x] Update `agent/PROCESS.md` **Plan mode / Approach** section: replace the topic-queue mechanic (Pending/Current, one topic per message, topics added-reordered-dropped) with the new draft-in-full + Unresolved mechanic, including the in-chat disclosure and the "delete Unresolved when Plan written" rule. Intent stage stays unchanged.
- [x] Update `agent/PROCESS.md` **Build mode / Executing** section: tick tasks in the change doc, post concise progress updates, interact mid-build only for surprises or plan problems. Keep the Feedback escape hatch as written.
- [x] Update `agent/PROCESS.md` to state that Approach and Plan drafts are written into the change document before approval is requested — not drafted in chat.
- [x] Scan `agent/README.md`, `agent/MAP-GUIDANCE.md`, `agent/PRINCIPLES.md`, and `agent/ADDITIONAL/*` for references to the old topic-queue mechanic or close-watching build language; update any that are stale.
- [x] Apply the new rule to this change itself: remove the `## Unresolved` section from `changes/open/refine-approach-and-build-cadence.md`.

## Conclusion

The scan task surfaced one surprise: `PRINCIPLES.md` presented the topic-queue mechanic as a foundational principle ("Interaction grain size"), not just a mechanism in `PROCESS.md`. After checking in, the section was recast to scope the principle explicitly to **map maintenance**, replacing the topic-queue wording with the one-node-at-a-time language that already matches `MAP-GUIDANCE.md`, and cross-referencing `PROCESS.md` for the Approach mechanic.

One follow-up was deferred: restoring a map-scoped "visible list of pending nodes" rule in `MAP-GUIDANCE.md` and `PRINCIPLES.md`. Captured as a draft note in `changes/open/map-update-visible-pending-list.md`.
