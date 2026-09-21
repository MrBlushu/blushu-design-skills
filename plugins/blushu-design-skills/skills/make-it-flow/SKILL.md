---
name: make-it-flow
description: Select, compare, compose, specify, implement, and verify interaction patterns for screen-based interfaces. Use when choosing or revising navigation, screen structure, workflows, list/detail behavior, action and state models, forms, data exploration, feedback and recovery, responsive adaptations, or whether an implementation preserves interaction state, especially when alternatives have meaningful tradeoffs or behavior is unresolved. Do not use for product discovery, generic usability audits without a pattern decision, purely aesthetic polish, text-only editing, accessibility certification, unrelated debugging, or mechanical implementation of an already complete interaction specification.
---

# Make It Flow

Turn a concrete interface problem into a coherent, testable interaction model. Implement only when the user explicitly requests a build or change; keep review and advice read-only.

## Resolve the execution profile

Resolve this before loading references or inspecting the project or artifact:

- **create:** produce a new interaction decision, specification, or blueprint; write only when the task authorizes an artifact;
- **change:** revise or implement an existing interaction within the named scope, but write only with separate task-supplied authorization;
- **review:** inspect a supplied interaction for evidence-backed mismatches without modifying files;
- **verify:** test only declared states, transitions, navigation, input, feedback, recovery, or continuity criteria on completed work; always remain read-only.

Map the previous `design` mode to `create`, and `revision` or `implementation` to `change`; implementation still requires explicit write authorization. Treat a focused decision as a scope modifier. Choose the profile from an explicit token after the skill name, then an explicit handoff `Mode`, then unambiguous request language, otherwise preserve the existing design/review behavior.

After resolving any profile, require a concrete interaction task or question, usable scope or artifact, and any authority the profile needs. If the request or workflow handoff supplies only the skill name, profile token, or `Mode` without that task context, and no usable recent context resolves it, return only the resolved `Mode` or `Mode: unresolved`, `Status: NEEDS_TASK`, the missing task fields, and `Mutations: none`; then stop before inspecting artifacts, loading references, or routing work.

For a workflow `verify` handoff, require `Question`, `Scope`, `Baseline`, `Criteria`, `Authority: read-only`, `Locked Decisions`, `Invocation ID`, `Artifact Revision`, and `Pass Limit: 1`. Recover a direct conversational task from the immediately preceding context only when artifact, closed question, scope, baseline, and criteria have one strongly supported interpretation. Otherwise return only `Mode: verify`, `Status: NEEDS_TASK`, the missing fields, and `Mutations: none`.

In `verify`, check only declared criteria and directly affected neighboring state in one bounded pass. Use real behavior when the claim requires it and load only the relevant domain and verification references. Retry one tool action only for a clearly transient safe failure. Do not mutate files, designs, configuration, or external systems; do not compare new pattern candidates, redesign the flow, recommend or apply a repair, invoke another skill, or execute a handoff or `Next Task`.

End `verify` with `Mode`, terminal `Status: PASS | FAIL | BLOCKED`, checked `Scope`, criterion-specific `Evidence`, `Failed Criteria`, optional uninvestigated `Out-of-scope Signals`, `Owner` for a failure, and `Mutations: none`. `PASS` needs evidence for every criterion; use `BLOCKED` when decisive behavior, an artifact, or a required tool is unavailable.

This terminal report replaces the normal output. In `verify`, retain only domain evidence, state-model, selective reference, and verification rules needed for the declared criteria; skip candidate generation, pattern selection, composition, implementation, recommendations, routing, and handoffs.

## Workflow

1. **Set scope and mode.**
   - Use the resolved `create`, `change`, or `review` profile; `verify` follows the bounded contract above instead of this workflow.
   - Limit mixed requests to the interaction-pattern portion and name any necessary handoff.
   - Route away unresolved product discovery, pure visual direction, generic usability review, text editing, certification, and unrelated debugging.
   - If the primary request is a generic audit or asks for everything wrong without naming an interaction-pattern decision, stop after stating that boundary and the appropriate handoff. Do not manufacture a pattern decision from the artifact or produce audit findings.

2. **Inspect before proposing.**
   - Read supplied artifacts and search the workspace for the existing implementation before asking for more context.
   - Require a concrete artifact for implementation or review: repository files, a screenshot, prototype, flow, recording, or sufficiently detailed markup/specification.
   - Locate established components, routes, state ownership, data loading, empty/error states, and relevant tests.
   - Distinguish observed facts, supported inferences, assumptions, and unknowns.

3. **Capture the decision context.**
   - Record the task, actors, frequency, content scale, platform, input methods, state lifetime, latency, risk, and constraints only when they can change the choice.
   - Treat missing evidence as an assumption. Ask only when alternatives would produce materially different, costly, or irreversible work; otherwise choose a reversible default and flag it.

4. **Model the interaction before controls.**
   - List the relevant objects, actions, states, relationships, transitions, entry, exit, failure, and recovery.
   - Identify the dominant screen purpose and navigation topology when applicable.
   - Remove unnecessary steps or unclear state boundaries before selecting a pattern.

5. **Load references selectively.**
   - Use the routing rules below and read only the files needed for the current decision.
   - Do not load every reference or recite the reference set as a catalog.

6. **Compare viable candidates.**
   - Generate no more than three candidates, including a direct unnamed solution when it may be simpler.
   - Compare user and task fit, content, state, navigation, feedback, recovery, input parity, platform, latency, and technical cost.
   - Reject mismatched candidates explicitly and choose one; do not return a neutral menu.

7. **Specify each retained pattern.**
   - State: problem and context; observable fit signals; contraindications and failure modes; effects on content, state, navigation, and feedback; relevant variants; technical dependencies; observable verification criteria.
   - Write `not applicable` only with a reason. A pattern name without this record is incomplete.

8. **Compose the interaction.**
   - Define screens or regions, entry and exit, actions, state ownership, transitions, and responsive/input variants.
   - Resolve conflicts between patterns, including Back, Close, Cancel, Done, focus, shortcuts, gestures, and shared regions.
   - Coordinate loading, empty, success, error, retry, cancel, undo, persistence, and synchronization.
   - Preserve selection, location, uncommitted work, and relevant history across switches unless a deliberate reset is safer.

9. **Act according to mode.**
   - For `create`, deliver the decision and interaction blueprint.
   - For a read-only `change`, identify the current mismatch and the smallest coherent replacement without editing.
   - For an authorized `change`, reuse local conventions, edit the minimum coherent surface, and add or update proportionate tests.
   - For `review`, remain read-only and report evidence-backed mismatches and pass criteria. If the task asks to fix them, resolve the profile as `change` and require separate write authorization.

10. **Verify and report.**
    - Exercise the critical task and alternate paths that affect safety, continuity, recovery, input, responsiveness, or latency.
    - Prefer observable interface behavior over static code inference when a runnable surface exists.
    - Report in proportion to the task; do not narrate this workflow.

## Collaboration handoff

- Accept an optional handoff with goal, evidence, constraints, decisions, open risks, artifact paths, and one next task; verify the artifacts instead of treating the handoff as proof.
- Preserve facts, supported inferences, assumptions, unknowns, and prior decisions as distinct states. Reopen a prior decision only for new evidence or a blocking contradiction, and say why.
- Own functional regions, relationships, state, behavior, semantic order, and responsive interaction changes; leave tracks, spans, gutters, and query geometry to structural layout work.
- When structural layout is the next unresolved responsibility, produce a handoff of at most 400 words containing regions, invariants, DOM and focus order, states to preserve, responsive behaviors, constraints, risks, and artifact paths.
- Record retained patterns and rejected alternatives in `Decisions`; keep unverified behavior and missing cases in `Open Risks`.
- Set `Next Task` to one precise out-of-scope responsibility. Suggest an installed skill only when useful; otherwise name the capability. Do not require an upstream handoff or make later specialists mandatory.

## Decision order

Prioritize:

1. task completion, data integrity, and prevention of irreversible harm;
2. fit to known users, evidence, frequency, skill, and context;
3. state continuity, orientation, feedback, and recovery;
4. accessible input parity and platform conventions;
5. content scale, latency, and technical feasibility;
6. consistency with the product and design system;
7. learnability versus repeated-use efficiency;
8. visual novelty.

When candidates are equivalent, choose the simpler, conventional, and reversible option. Change a structural mismatch instead of compensating with explanatory copy.

## Reference routing

- Read [pattern-selection.md](references/pattern-selection.md) when requirements are sparse, multiple solutions are plausible, or a no-pattern option may win.
- Read [structure-and-navigation.md](references/structure-and-navigation.md) for screen purposes, workflow order, entry points, modes, hierarchy, parallel workspaces, orientation, or movement between places.
- Read [content-and-layout.md](references/content-and-layout.md) for functional hierarchy, disclosure, list/detail behavior, collections, pagination, or transformation across viewport sizes.
- Read [actions-and-state.md](references/actions-and-state.md) for command placement, asynchronous or destructive work, preview, progress, cancellation, undo, persistence, or cross-view continuity.
- Read [data-and-input.md](references/data-and-input.md) for data exploration, filtering, structured or forgiving entry, autocomplete, defaults, validation, and recoverable form errors.
- After the request passes the scope check, read [verification.md](references/verification.md) for every in-scope review and after implementation; use it for scenario coverage, transition checks, navigation continuity, input parity, responsive behavior, latency, and evidence-backed findings.

If a task crosses domains, load only the intersecting references and keep ownership explicit. Let content/layout choose the spatial relationship; let actions/state define what survives transitions.

## Output

Scale the response to the decision. For a small choice, provide context, decision, retained-pattern specification, and verification; keep each required field to a phrase when that is sufficient. For a workflow, revision, or implementation, use:

```markdown
## Context
Facts, assumptions, task, platform, and constraints that affect the decision.

## Pattern decision
Up to three candidates, rejected alternatives, and the final choice.

## Pattern specification
The complete seven-field record for each retained pattern.

## Interaction blueprint
Objects, actions, regions, navigation, states, transitions, recovery, and variants.

## Implementation
Files/components changed or exact guidance. Include only when relevant.

## Verification
Scenarios exercised, observable pass criteria, tests, and residual risks.
```

Use tables only for comparisons or state mappings that become clearer in tabular form. Cite real artifact paths and line numbers when reviewing or implementing.

## Quality rules

- Link every choice to the concrete task and available evidence; never invent research, personas, or user behavior.
- Resolve conflicting effects between selected patterns instead of listing them independently.
- Specify state, feedback, recovery, and technical consequences wherever they can affect the task.
- Verify current platform behavior, framework APIs, accessibility rules, and numeric requirements from authoritative current sources when they materially affect the decision.
- Never claim accessibility certification from this workflow.
- Preserve local product and code conventions unless they cause the interaction mismatch being fixed.
- Run proportionate tests and state untested conditions or residual risks.
- Keep implementation claims, review findings, and output length proportional to observed evidence and user impact.
