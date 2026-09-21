# Verification execution profile

Status: approved for implementation on `develop` (2026-09-18)

## Context

Blushu Design Skills currently combines seven portable skills: six specialists and the `lets-build-a-site` orchestrator. The skills already define responsibility boundaries, evidence rules, scoped read-only reviews, implementation behavior, verification steps, and compact handoffs. They do not share one explicit invocation contract for a skill called from an automated workflow with only a mode token such as `make-it-obvious verify`.

The observed failure is specific: when a skill is inserted into a verification workflow after work is already complete, but receives no concrete task message, it can spend excessive time reconstructing intent. It may broaden a closed verification into a review, recommend a correction, emit a handoff, reopen an earlier discipline, or repeat checks. The repository's existing forward tests used normal user requests and therefore do not cover this bare or workflow-generated invocation path.

## Goal

Add a shared execution-profile contract so every skill can distinguish creation, change, open review, and closed verification. A direct invocation such as `make-it-obvious verify` should verify the immediately preceding scoped work when the artifact and acceptance criteria are unambiguous in the current context. It must otherwise stop with `NEEDS_TASK` rather than inventing scope.

The change must make verification bounded, read-only, evidence-based, and terminal while preserving normal natural-language use of every skill.

## Users and systems affected

- A person invoking a Blushu skill directly after making a change.
- `lets-build-a-site` or another automated workflow invoking a specialist.
- Codex and Claude Code sessions loading the portable `SKILL.md` files.
- Maintainers who need one consistent contract across all seven skills.

## Verified current state

Verified on 2026-09-15 against commit `f85dddc`:

- `make-it-flow`, `set-the-grid`, and `check-the-style` already infer local operating modes, but their mode names and rules differ.
- `before-we-make-a-mess`, `make-it-obvious`, `break-it-right`, and `lets-build-a-site` do not define the proposed common four-profile contract.
- `make-it-obvious` is an open usability review workflow and does not distinguish a closed regression verification from a new review.
- `break-it-right` contains broad correction and rendering instructions without an explicit read-only verification profile.
- `lets-build-a-site/references/specialist-routing.md` requires one owned question and allows a transient retry, but it can route an out-of-scope dependency and return to the interrupted task. It does not carry an invocation identity, artifact revision, pass limit, or terminal verification rule.
- The repository has no committed behavioral evaluation suite for bare or mode-only invocations.

## Decisions

### One common profile vocabulary

All seven skills must recognize the same four profiles:

| Profile | Intent | Default authority | Completion condition |
| --- | --- | --- | --- |
| `create` | Produce a new decision, design, specification, or artifact | Read-only unless the task explicitly authorizes creation or writes | Requested artifact or decision is produced and its limits are stated |
| `change` | Modify an existing artifact within a named scope | Scoped write | Change is applied and the affected surface is checked |
| `review` | Search an artifact for relevant problems without a closed claim | Read-only | Prioritized findings and their evidence are reported |
| `verify` | Test declared claims or acceptance criteria on completed work | Read-only | `PASS`, `FAIL`, or `BLOCKED` is returned for the declared criteria |

Profile and authority are separate. A profile never grants broader write permission than the task supplies. `verify` is always read-only, even when the underlying skill normally supports implementation.

### Profile resolution

Resolve the profile in this order:

1. an explicit profile in the current request, including a token immediately following the skill name;
2. an explicit `Mode` field in a workflow handoff;
3. an unambiguous natural-language request;
4. the skill's existing default behavior for normal interactive requests.

Do not infer a task from the skill name alone. A workflow invocation that supplies no concrete question and no usable recent context must return `NEEDS_TASK`.

### Minimum invocation contract

A workflow handoff may keep the existing fields, but must add the following fields when it invokes a skill in `verify`:

```text
Mode: verify
Question: one closed claim or verification question
Scope: artifact paths plus relevant task, states, widths, or components
Baseline: prior finding, accepted requirement, or artifact revision
Criteria: observable pass/fail conditions
Authority: read-only
Locked Decisions: accepted decisions that must not be reopened
Invocation ID: identifier for this specialist pass
Artifact Revision: commit, hash, mtime set, or another stable revision marker
Pass Limit: 1
```

The artifact, question, and criteria may be recovered from the immediately preceding conversation or handoff only when one interpretation is strongly supported. If multiple artifacts or competing criteria remain plausible, return `NEEDS_TASK` with only the missing fields.

### Verify profile behavior

In `verify`, every skill must:

1. inspect only the declared criteria and the directly affected neighboring state;
2. load only references needed by those criteria;
3. use real artifact or rendered evidence when the claim requires it;
4. perform one bounded verification pass;
5. retry a tool action once only when the failure is clearly transient and safe;
6. make no file, design, configuration, external-system, or handoff mutation;
7. avoid open-ended discovery, redesign, reprioritization, or a full review;
8. preserve all locked decisions unless reporting a direct contradiction as evidence;
9. never invoke another skill or automatically execute a `Next Task`;
10. terminate with the common output contract.

A possible out-of-scope regression may be reported as an uninvestigated signal. It must not expand the verification scope.

### Common terminal output

Use the smallest report that preserves:

```text
Mode: verify
Status: PASS | FAIL | BLOCKED
Scope: artifacts, criteria, states, and widths actually checked
Evidence: commands, rendering, measurements, or inspected signals
Failed Criteria: only failed criteria, or none
Out-of-scope Signals: optional and explicitly uninvestigated
Owner: responsible skill or capability when status is FAIL
Mutations: none
```

`PASS` requires named evidence for every declared criterion. `FAIL` means at least one criterion was contradicted. `BLOCKED` means the criterion was valid but could not be evaluated with available evidence or tools. `NEEDS_TASK` is a preflight result used only when no concrete verification task can be resolved.

## Orchestrator anti-loop rules

`lets-build-a-site` must generate a concrete invocation message rather than forwarding only a skill name. Its routing contract must enforce:

- one specialist and one owned question per invocation;
- no second invocation with the same `Invocation ID`;
- no reinvocation of the same skill when `Artifact Revision` is unchanged;
- a failed verification terminates the verification step and names the owner without starting a repair;
- repair, when authorized, is a separate `change` invocation;
- after a repair, one targeted `verify` invocation is allowed against a new artifact revision;
- the maximum automatic sequence is `verify -> change -> verify`, after which the workflow stops and reports the unresolved result;
- a handoff emitted or suggested during verification is informational and cannot trigger another specialist;
- the smallest failed check is rerun after a change; a full specialist pass requires a systemic change and an explicit new question.

The orchestrator must keep the sequence ledger in memory from the initial `verify` through its optional authorized `change` and single targeted reverification so tracking cannot mutate the repository or alter an artifact revision. Persistence is allowed only later as separately authorized non-verify orchestration work. Each entry contains sequence ID, invocation ID, origin verification ID, skill, profile, question, scope, stable criterion IDs, per-criterion outcomes including failed criterion IDs, verification ordinal, artifact revision, result, and next authorized action. Duplicate detection uses skill, criterion IDs, scope, and artifact revision rather than mutable question wording. Validate the one-repair limit before dispatching a `change`. Verification of that change's output must retain the same sequence and origin verification IDs and use ordinal 2; it cannot reset as a fresh sequence. Close the sequence after ordinal 2 or when no repair is authorized. The ledger must not copy skill output or become a second handoff format. Artifact revision markers exclude ledger and orchestration metadata.

## Skill-specific mappings

The common contract controls execution. Each skill keeps ownership of what evidence and criteria mean in its domain.

| Skill | `verify` checks | It must not become |
| --- | --- | --- |
| `before-we-make-a-mess` | whether named decision-gate conditions and evidence claims are supported | renewed opportunity discovery or a new research program |
| `make-it-flow` | whether specified states, transitions, navigation, input, feedback, and recovery remain intact | a fresh pattern comparison or redesign |
| `set-the-grid` | whether declared containers, spans, alignments, thresholds, order, and overflow criteria hold | a new grid derivation |
| `check-the-style` | whether approved visual changes and named viewport/state criteria render as intended | an open visual audit or polish pass |
| `make-it-obvious` | whether named usability findings or task-path corrections are resolved in the supplied states | a new whole-interface usability review |
| `break-it-right` | whether named text blocks wrap correctly with the actual font and project widths | global typography, copy, or grid revision |
| `lets-build-a-site` | whether declared website acceptance criteria and final QA claims hold | a rebuild, redesign, or new specialist pipeline |

## Implementation plan

### Phase 0: capture the baseline

Before editing any skill, run the nine primary behavior cases against the current plugin in fresh sessions. Record status, actions/tool calls, elapsed time, mutations, specialist reinvocations, and final output. Preserve the prompts and results under ignored working artifacts, not in the distributable skill package.

### Phase 1: contract and MVP

1. Add the common execution-profile block to `make-it-obvious`, `check-the-style`, and `break-it-right`.
2. Reconcile existing local mode wording instead of adding a second competing mode system.
3. Add the detailed invocation envelope and anti-loop behavior to `lets-build-a-site/references/specialist-routing.md`.
4. Add the corresponding high-level orchestration rule to `lets-build-a-site/SKILL.md`.
5. Run the nine primary candidate cases and compare them with the baseline.

Do not continue to Phase 2 unless all safety gates pass and the action-count target is met.

### Phase 2: complete the suite

Apply the same short contract to `before-we-make-a-mess`, `make-it-flow`, `set-the-grid`, and `lets-build-a-site`. Preserve each skill's existing specialist workflow and terminology below the shared profile layer.

### Phase 3: documentation, validation, and release preparation

1. Document direct `review`, `change`, and `verify` examples in `README.md` and `examples/existing-project.md`.
2. Add a deterministic standard-library validation script at `scripts/check-execution-profiles.py` to confirm that all seven skills expose the required profiles, no-task guard, read-only verification rule, and terminal statuses.
3. Add a committed behavioral test matrix at `tests/execution-profiles.md`; keep generated transcripts, screenshots, caches, and local installations ignored.
4. Validate every `SKILL.md` with the canonical skill validator.
5. Validate both plugin manifests and perform a clean local Codex plugin installation from the repository checkout.
6. Run one normal non-verify smoke request per skill to detect regressions in existing behavior.
7. Run the full verification matrix in fresh Codex sessions.
8. If all gates pass, update both plugin versions from `0.1.0` to `0.2.0` and add a concise release note to the README or a changelog if one is introduced during implementation.

Model-backed Claude behavior testing is not required for the MVP gate, but the portable files and Claude manifest must remain valid. Any untested Claude behavior must be reported before release.

## Files expected to change

| File or family | Planned change |
| --- | --- |
| `plugins/blushu-design-skills/skills/*/SKILL.md` | Shared profiles, `NEEDS_TASK` guard, and terminal `verify` behavior in all seven skills |
| `plugins/blushu-design-skills/skills/lets-build-a-site/references/specialist-routing.md` | Invocation envelope, revision tracking, and anti-loop rules |
| `README.md` | Explain profiles and direct verification usage |
| `examples/existing-project.md` | Add reusable profile-specific prompts |
| `scripts/check-execution-profiles.py` | Deterministic contract validation |
| `tests/execution-profiles.md` | Behavioral prompt matrix and expected outcomes |
| `.claude-plugin/marketplace.json` | Version `0.2.0` after release gates pass |
| `plugins/blushu-design-skills/.codex-plugin/plugin.json` | Version `0.2.0` after release gates pass |
| `plugins/blushu-design-skills/.claude-plugin/plugin.json` | Version `0.2.0` after release gates pass |

Do not change `agents/openai.yaml` unless testing proves that host-generated default prompts prevent explicit profile resolution. Do not duplicate the detailed orchestration envelope in all specialist skills.

## Behavioral evaluation matrix

### Nine primary cases

Run each of `make-it-obvious`, `check-the-style`, and `break-it-right` against:

1. a completed change that satisfies all supplied criteria, expecting `PASS`;
2. a completed change with one seeded domain-specific failure, expecting `FAIL` and the correct owner;
3. a valid criterion that cannot be tested with available evidence, expecting `BLOCKED`.

The same nine prompts and fixtures must be used before and after implementation.

### Seven no-task cases

Invoke each skill with only its name and no resolvable recent task. Expect `NEEDS_TASK`, no reference expansion beyond preflight, no mutation, and no specialist routing.

### Three orchestration cases

1. A failed verification reports the owner and stops without repair.
2. A repeated invocation with the same artifact revision is rejected without rerunning the specialist.
3. A separately authorized repair produces a new revision and permits exactly one targeted reverification.

## Acceptance criteria

1. All seven skills recognize `create`, `change`, `review`, and `verify` with the same meaning and without overriding narrower write authorization.
2. `make-it-obvious verify` uses an unambiguous immediately preceding artifact and criteria, remains read-only, and returns a terminal status without opening a new usability review.
3. Every no-task case returns `NEEDS_TASK` and performs no mutation or cross-skill routing.
4. All nine primary candidate cases return the expected `PASS`, `FAIL`, or `BLOCKED` result.
5. Every `verify` case records `Mutations: none`; repository and artifact hashes confirm no changes.
6. No `verify` case invokes another skill, executes a handoff, or exceeds one bounded pass.
7. The orchestrator rejects an unchanged repeated invocation and permits one reverification only after a separately authorized change produces a new revision.
8. Median agent action count across the nine primary cases is at least 30% lower than the current baseline. Wall-clock time is recorded as a secondary metric but is not a release blocker because host latency varies.
9. Normal non-verify smoke requests for all seven skills retain their existing domain ownership, evidence rules, and write boundaries.
10. The deterministic contract script, canonical skill validation, plugin manifest validation, and clean local Codex installation all pass.
11. README and examples describe the difference between open `review` and closed `verify`, including the `NEEDS_TASK` fallback.
12. Version metadata changes to `0.2.0` only after every required gate passes.

## Out of scope

- Changing the domain methodology or ownership boundaries of any skill.
- Automatically repairing a failed verification.
- Automatically invoking another skill from `verify`.
- Building a general workflow engine outside `lets-build-a-site`.
- Persisting full prompts or model outputs inside the published plugin.
- Making the seven skills depend on one shared runtime file outside their own portable directories.
- Publishing, pushing, opening a pull request, or merging to `main` as part of this specification step.
- Requiring model-backed Claude behavior tests for the MVP gate.

## Rollback

Keep the work in coherent commits on `develop`: baseline/tests, MVP profiles, remaining profiles, then documentation/version. If the MVP gates fail, revert the MVP commit while retaining the baseline fixtures and report. If a later skill regresses, revert only that skill's profile change and leave version metadata at `0.1.0`. The final release can be rolled back by reverting the merge commit or release commit; no data migration or external state is involved.

## Git delivery strategy

- Source branch: `develop`, created from `main` at `f85dddc`.
- Do not edit or commit directly on `main`.
- Do not treat personal installed skill copies as the source of truth.
- Implement and validate the repository copies under `plugins/blushu-design-skills/skills/`.
- Keep commits single-purpose and do not combine the implementation with unrelated laboratory artifacts.
- Push `develop` only after local validation, then open a reviewable pull request from `develop` to `main`.
- Do not force-push or rewrite published history.

## Start prompt for the implementation session

Use this from the repository root on or after 2026-09-19:

```text
Work on the current `develop` branch and implement `docs/verify-execution-profile-spec.md` completely.

Start by verifying the repository state, current commit, and that the working tree contains no unrelated changes. Read the full specification and the seven current SKILL.md files before editing. Treat the repository copies as the source of truth; do not edit personal installed skills first.

Capture the required baseline behavior before changing the skills. Then implement Phase 1 only and run its release gates. Continue to the remaining phases only if the MVP gates pass. Keep `verify` read-only, bounded to one pass, terminal, and unable to invoke other skills. Preserve every skill's existing ownership and normal non-verify behavior.

Use coherent commits on `develop`. Do not push, publish, open a pull request, or merge unless I explicitly request it. Finish with the acceptance-criteria results, before/after action counts, files changed, commits created, untested conditions, and the exact next Git step.
```
