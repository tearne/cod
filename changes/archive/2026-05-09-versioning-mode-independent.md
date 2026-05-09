# Versioning mode-independent

**Mode:** Formal

## Intent

The change-modes work tied versioning to the Plan stage by leaving the existing wording untouched ("the Plan includes a task to bump version"). Wander has no Plan, so a Wander change can ship a behaviour change to a versioned project without a version bump — exactly what happened to `sysmon` (0.3.0) in hub75 on 2026-05-05.

Make versioning mode-independent: if versioning is in effect, every hand-back of code to the user carries an appropriate version bump, regardless of mode. The mechanism shouldn't depend on a Plan stage existing.

Origin: hub75 process-feedback (2026-05-05) raised after a Wander change shipped without a bump.

## Approach

### Versioning is a Build-mode concern

Move responsibility for proposing/executing the bump out of the Plan stage and into Build mode, where it applies to any mode uniformly. The Plan-stage clause "the Plan includes a task to bump version" is removed.

### Bump on entering Build

On entering Build, the agent announces the proposed bump kind against the current latest version, asks the user to approve, and writes the version. Code in development needs the right version baked in for tests and dependency declarations.

### Patch bump on every test hand-back

Every time the agent hands back to the user for testing — initial completion or any subsequent tweak — the patch version is bumped. The user can then tell at a glance whether they are seeing the latest build. The final tested value is what ships.

## Plan

- [x] Remove the Plan-stage versioning clause from `PROCESS.md`.
- [x] Rewrite the Build-mode versioning paragraph to cover bump-kind approval on entry (any mode) and patch bump on every test hand-back.
- [x] Bump version (date-based, kind: patch — guidance refinement). → 2026-05-09.1

## Log

- Adjacent fix: "On Plan approval, create `active.md`" in Entering build now reads "On approval to enter Build (Plan approval for Formal/Explore, Intent approval for Wander)" — same Wander-doesn't-have-a-Plan gap as the versioning issue.

## Conclusion

Completed. Adjacent fix to Entering build wording captured in the Log.

Proposed changelog entry (2026-05-09.1):

> `PROCESS.md`: versioning is now a Build-mode concern, not a Plan-stage one. On entering Build the agent proposes a bump kind, gets user approval, and writes the version — same flow in any mode (Formal/Explore/Wander). Every subsequent test hand-back bumps patch so the user can tell at a glance whether they are seeing the latest build. Adjacent fix: Entering build's "On Plan approval" trigger generalised to cover Wander (Intent approval).
