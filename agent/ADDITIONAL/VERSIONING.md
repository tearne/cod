# Versioning

Use [Semantic Versioning](https://semver.org/): `MAJOR.MINOR.PATCH`.

| Segment | Increment when |
|---------|---------------|
| `MAJOR` | Breaking changes — existing behaviour is removed or incompatibly changed |
| `MINOR` | New functionality added in a backwards-compatible way |
| `PATCH` | Corrections, tweaks, and bug fixes |

Start at `0.1.0` if the project is not yet stable, or `1.0.0` for a first stable release.

When in doubt, prefer a patch bump — it is always safe to increment patch, and version numbers are cheap.

## Negotiated Bumps

When a project manages releases manually, agree the bump level with the user at implementation kickoff based on what the accumulated changes represent. It is acceptable for the agreed level to change as implementation progresses.

Add this to the kickoff checklist at `Designing → Implementing`:
- **Version bump** — major, minor, or patch? Agree based on the nature of the change; revisit if scope changes during implementation.
