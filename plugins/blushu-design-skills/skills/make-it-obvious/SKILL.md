---
name: make-it-obvious
description: Review concrete web and mobile interfaces, flows, prototypes, recordings, and usability-test notes for comprehension, orientation, action clarity, and avoidable task friction. Use for usability reviews, diagnosing hesitation, missed actions, navigation failures, or recoverable errors, and turning observed behavior into prioritized local improvements. Do not use for product discovery, interaction systems designed from scratch, visual-only polish, final text composition, performance engineering, or accessibility certification.
---

# Make It Obvious

Review a concrete interface against realistic user tasks. Diagnose avoidable interpretation, orientation, and interaction costs. Recommend the smallest causal correction and an observable verification.

## Resolve the execution profile

Resolve this before loading references or inspecting the artifact:

- **create:** produce a new usability decision, test plan, or review artifact; write only when the request authorizes it;
- **change:** apply a requested modification within the named scope, but write only with separate task-supplied authorization;
- **review:** search the supplied interface for relevant usability problems without a closed claim; remain read-only;
- **verify:** test only declared usability claims or acceptance criteria on completed work; always remain read-only.

Choose the profile from an explicit token after the skill name, then an explicit handoff `Mode`, then unambiguous request language, otherwise use the existing review behavior. A focused request is not permission to write.

If the current request supplies only the skill name and an optional profile token, with no usable recent task or handoff, return only the resolved `Mode` or `Mode: unresolved`, `Status: NEEDS_TASK`, the missing task fields, and `Mutations: none`; then stop before inspecting artifacts or loading references.

For a workflow `verify` handoff, require `Question`, `Scope`, `Baseline`, `Criteria`, `Authority: read-only`, `Locked Decisions`, `Invocation ID`, `Artifact Revision`, and `Pass Limit: 1`. A direct conversational invocation may recover the artifact, closed question, scope, baseline, and criteria from the immediately preceding context only when one interpretation is strongly supported.

If a concrete verification task cannot be resolved, return only `Mode: verify`, `Status: NEEDS_TASK`, the missing task fields, and `Mutations: none`; then stop without loading conditional references, inspecting unrelated files, routing work, or proposing a review.

In `verify`:

1. Check only the declared criteria and directly affected neighboring state, using the minimum evidence and references needed.
2. Run one bounded pass. Retry one tool action only for a clearly transient safe failure.
3. Do not mutate files, designs, configuration, or external systems; do not broaden into a review; do not recommend or apply a repair; do not invoke another skill; and do not execute a handoff or `Next Task`.
4. Preserve locked decisions. Report a possible adjacent regression only as an uninvestigated out-of-scope signal.
5. End with `Mode`, terminal `Status: PASS | FAIL | BLOCKED`, checked `Scope`, criterion-specific `Evidence`, `Failed Criteria`, optional `Out-of-scope Signals`, `Owner` for a failure, and `Mutations: none`. `PASS` needs evidence for every criterion; use `BLOCKED` when decisive evidence or a required tool is unavailable.

This terminal verify report replaces the normal review output below. In `verify`, skip open discovery, whole-interface review, finding prioritization, recommendations, handoffs, and normal review output. Still apply the domain evidence distinctions, claim-matched verification rules, selective reference loading, and non-routing quality rules below when they are necessary for the declared criteria. Never apply a later rule that routes, invokes, hands off, recommends a repair, or mutates; report the underlying barrier only as an uninvestigated out-of-scope signal.

## Establish scope

1. Identify the artifact, task, platform or viewport, entry point, covered states, and constraints.
2. Separate facts, observed behavior, measurements, inferences, and assumptions. Never present predicted behavior as observed.
3. Use `observed` only for supplied human behavior. For a static artifact, describe the visible UI as the signal and label its predicted task consequence `inferred`.
4. Infer missing context only when one interpretation is strongly supported. State the assumption; ask only when alternatives materially change the review.
5. Exclude product desirability, interaction-system design, visual styling, full copy composition, performance optimization, and accessibility certification. For mixed requests, complete the usability diagnosis and hand off the rest. Redirect purely out-of-scope requests without inventing a review.

## Review the interface

1. Inspect the whole composition first. Check identity, purpose, priority, regions, actions, and the start or continuation point.
2. Walk each task state by state, including deep entry and recovery. Check label promises, choice consequences, visible state, feedback, error prevention, and repair.
3. Record only avoidable task costs. Preserve necessary domain complexity, safety steps, useful density, and short deviations with easy recovery.

## Load references selectively

- Read [clarity-and-action.md](references/clarity-and-action.md) for first-glance or single-screen hierarchy, scanning, labels, choices, controls, affordances, or local noise.
- Read [orientation-and-navigation.md](references/orientation-and-navigation.md) only for home or landing comprehension, multiple pages, deep links, global or local navigation, location cues, browse, or search.
- Read [friction-and-trust.md](references/friction-and-trust.md) only for multi-step tasks, forms, consequential choices, errors, mobile constraints, waits, transparency, or recovery.
- Read [observational-evidence.md](references/observational-evidence.md) only for supplied behavioral evidence or a requested lightweight user test. Do not load it merely because a static finding is inferred.
- Load more than one reference only when the task spans their conditions. Do not load all references by default.

## Form and prioritize findings

1. Tie every finding to an element, state, or supplied behavior. Exclude aesthetic preferences without task impact and rules without a concrete signal.
2. Group symptoms by likely cause; separate those requiring different corrections.
3. State task impact, scope, recovery cost, and confidence. Distinguish observed problems from inferred risks.
4. Use severity bands without fabricated scores:
   - **Critical:** blocks an essential task, creates a severe error, or prevents recovery.
   - **High:** frequently diverts the task, hides required information, or creates costly uncertainty.
   - **Medium:** causes hesitation or delay while leaving a recognizable, recoverable path.
   - **Low:** creates limited local friction; include only when the correction is clear and does not distract from serious issues.
5. Break ties by breadth, repetition, entry-point impact, and recovery difficulty. Keep implementation ease separate from severity.

## Recommend and verify

- Prefer the smallest local change that removes the cause. Subtract obstruction before adding instructions.
- Fix causal labels or instructions; leave full microcopy and line composition outside scope.
- Preserve valid tradeoffs and complexity. Do not prescribe minimalism, fewer clicks, shorter copy, or more whitespace without a task benefit.
- Stop at diagnosis when a fix changes information architecture, interaction model, or pattern system. Hand off the problem, constraints, evidence, artifact paths, and design question.
- Match verification to the claim: inspection for visible clarity, walkthrough or first click for navigation, completion and recovery for flows, or a reliable behavioral metric.
- Claim no improvement in trust, comprehension, or success without an observable signal.

## Collaboration handoff

- Accept an optional handoff with goal, evidence, constraints, decisions, open risks, artifact paths, and one next task; inspect the referenced interface and states rather than treating the handoff as observed behavior.
- Preserve facts, reported or measured behavior, inferences, assumptions, and prior decisions as distinct states. A prior visual or interaction change is not evidence of improvement until the relevant task signal is checked.
- Keep local causal fixes separate from findings that require a new interaction pattern, coordinated grid change, visual-system correction, copy work, or line composition.
- When another responsibility remains, produce a handoff of at most 400 words with the finding, evidence class, task impact, constraints, decisions to preserve, residual risk, artifact paths, and one verification question.
- List visible text for line-composition work only when a concrete wrapping, orphan, balance, or overflow signal exists; do not pass a generic text inventory.
- Set `Next Task` to one precise out-of-scope responsibility. Suggest an installed skill only when useful; otherwise name the capability. Do not require an upstream handoff or a fixed pipeline.

## Output

Scale the report. Start with:

- artifact and tasks covered;
- main usability risk;
- what should be preserved;
- evidence limitations and assumptions.

For a formal or multi-finding review, use:

```markdown
## [Critical | High | Medium | Low] Problem-oriented title
Evidence: observed | reported | measured | inferred
Signal: concrete element, state, or behavior
Task impact: consequence for the person
Recommendation: smallest local correction
Verification: check that can confirm or falsify improvement
Confidence: high | medium | low
```

For a small review, compress the same fields into bullets but preserve evidence class, task impact, recommendation, and verification.

Close with unverified hypotheses, tradeoffs to preserve, and any handoff. If no serious issue is supported, say so.

## Quality rules

- Base each finding on the supplied artifact or evidence, not a universal checklist.
- Never infer prevalence from a small qualitative sample or certify compliance from an interface review.
- Do not invent sample sizes, success quotas, or pass thresholds. Use supplied baselines or state the behavior that would confirm or falsify the change.
- Flag evident accessibility barriers, then route formal WCAG or legal assessment to a specialist.
- Use concrete language. Never recommend only to “improve the UX.”
