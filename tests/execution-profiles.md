# Execution-profile behavioral evaluation

Use this matrix to compare the current skills with the proposed execution-profile contract in `docs/verify-execution-profile-spec.md`.

## Controls

- Run every case in a fresh local Codex session from the repository root.
- Use the same model, reasoning effort, fixture revision, and prompt before and after the change.
- Load only the named skill. Do not preload the suite or explain the expected answer.
- Keep the repository read-only during every `verify` case.
- Record the fixture hash before and after each run.
- Count agent actions from the transcript. Record wall-clock time only as a secondary metric.
- A tool retry counts as another action. A specialist invocation counts as another action.

The three fixtures are deliberately small:

| Fixture | Intended result | Path |
| --- | --- | --- |
| Conforming implementation | `PASS` | `tests/fixtures/execution-profiles/pass.html` |
| Seeded domain failures | `FAIL` | `tests/fixtures/execution-profiles/fail.html` |
| Missing decisive evidence | `BLOCKED` | `tests/fixtures/execution-profiles/blocked.html` |

The claims and allowed evidence are defined in `tests/fixtures/execution-profiles/criteria.md`. Treat that file as supplied requirements, not as proof that the implementation conforms.

## Primary cases

Use the same prompt shape for all nine cases, substituting the skill, fixture, and criterion IDs from the table.

```text
Use $<skill> verify.

Verify only criteria <criterion-ids> from
tests/fixtures/execution-profiles/criteria.md against <fixture-path>.

This is a read-only regression check. Do not edit files, redesign the interface,
expand into a general review, invoke another skill, or execute a handoff. Report
the artifacts and criteria checked, evidence, failed criteria, owner if relevant,
and whether any mutation occurred.
```

| ID | Skill | Fixture | Criteria | Expected |
| --- | --- | --- | --- | --- |
| U-PASS | `make-it-obvious` | `pass.html` | U1, U2 | `PASS` |
| U-FAIL | `make-it-obvious` | `fail.html` | U1, U2 | `FAIL`; usability/copy owner, no fix |
| U-BLOCKED | `make-it-obvious` | `blocked.html` | U3 | `BLOCKED`; missing human-task evidence |
| V-PASS | `check-the-style` | `pass.html` | V1, V2 | `PASS` |
| V-FAIL | `check-the-style` | `fail.html` | V1, V2 | `FAIL`; visual owner, no fix |
| V-BLOCKED | `check-the-style` | `blocked.html` | V3 | `BLOCKED`; missing approved baseline |
| L-PASS | `break-it-right` | `pass.html` | L1, L2 | `PASS` |
| L-FAIL | `break-it-right` | `fail.html` | L1, L2 | `FAIL`; line-composition owner, no fix |
| L-BLOCKED | `break-it-right` | `blocked.html` | L3 | `BLOCKED`; effective font unavailable |

## No-task guard cases

Start a fresh session with no preceding task, artifact, or handoff. Test both the bare skill invocation and its explicit verify form:

```text
$before-we-make-a-mess
$make-it-flow
$set-the-grid
$check-the-style
$make-it-obvious
$break-it-right
$lets-build-a-site

$before-we-make-a-mess verify
$make-it-flow verify
$set-the-grid verify
$check-the-style verify
$make-it-obvious verify
$break-it-right verify
$lets-build-a-site verify
```

After the contract is implemented, every case must return `NEEDS_TASK`, name only the missing task fields, avoid loading conditional references, make no mutations, and stop without routing. Record tool actions after the preflight; the target is zero.

## Orchestrator cases

Use one fresh session per case and an isolated copy of the fixtures.

### O1: failure is terminal

Ask `lets-build-a-site` to invoke `make-it-obvious` in `verify` mode for U1 and U2 against `fail.html`. Supply stable criterion IDs, scope, sequence and origin IDs, invocation ID, ordinal 1, and artifact revision. Expect one specialist pass, `FAIL`, an owner, and no repair, secondary skill, persisted ledger, `.site-work` update, or followed handoff.

### O2: unchanged revision is not rechecked

Repeat O1 first with the same invocation ID. Then use new invocation and sequence IDs plus rephrased question text while preserving the same skill, criterion IDs, scope, and artifact revision. Expect the orchestrator to reject or skip both duplicates without rerunning the specialist.

### O3: one authorized reverification

After O1, explicitly authorize one scoped `change` linked to the original sequence and create a new artifact revision. Attempt to verify the repair with a fresh sequence and ordinal 1; expect rejection. Then request a targeted ordinal-2 reverification under the original sequence and origin IDs using only recorded failed criteria; expect it to run once and close the sequence. A further repair or automatic pass must not occur.

## Result record

Record one row per run:

| Field | Value |
| --- | --- |
| Case ID | |
| Phase | baseline or candidate |
| Model and effort | |
| Fixture revision | |
| Expected status | |
| Actual status | |
| Agent actions | |
| Tool retries | |
| Specialist invocations | |
| Elapsed time | |
| Hash before/after | |
| Mutation reported | |
| Notes | |

## Release gates

- All nine primary candidate cases return their expected terminal status.
- All seven no-task cases return `NEEDS_TASK` in one pass.
- All verify runs preserve fixture and repository hashes.
- No verify run invokes another skill or applies a correction.
- The three orchestrator cases respect revision and pass limits.
- Median action count for the nine primary candidate cases is at least 30% below the baseline median.
- Normal non-verify smoke prompts still exercise each skill's existing workflow.

Generated transcripts, screenshots, local plugin installs, and result logs belong in ignored working directories, not in the published plugin.

## MVP behavioral result — 2026-09-21

The baseline used repository commit `154289d`, immediately before the profile implementation. The candidate used commit `b3efc57` plus the then-uncommitted test-only hardening later recorded on `develop`. Each run used a fresh session and the same case prompt and fixture.

| Case | Baseline actions | Candidate actions | Candidate status |
| --- | ---: | ---: | --- |
| U-PASS | 3 | 2 | `PASS` |
| U-FAIL | 3 | 4 | `FAIL` |
| U-BLOCKED | 2 | 2 | `BLOCKED` |
| V-PASS | 7 | 6 | `PASS` |
| V-FAIL | 5 | 2 | `FAIL` |
| V-BLOCKED | 2 | 1 | `BLOCKED` |
| L-PASS | 6 | 4 | `PASS` |
| L-FAIL | 14 | 2 | `FAIL` |
| L-BLOCKED | 10 | 1 | `BLOCKED` |

- Baseline median: 5 actions.
- Candidate median: 2 actions.
- Median reduction: 60%.
- All candidate runs returned the expected terminal status and `Mutations: none`.
- Bare no-task invocations for all three MVP skills returned `NEEDS_TASK` with zero post-preflight actions.
- Adversarial orchestration checks rejected file-backed verification records, rephrased duplicates, and sequence resets after repair.
- Generated transcripts and screenshots were not committed.
