---
name: before-we-make-a-mess
description: Guide product discovery for uncertain opportunities, features, and UX/UI directions by framing the problem, target users, outcomes, alternatives, evidence, assumptions, and risks; choose focused research, experiments, or prototypes and define decision gates before interaction design or further product investment. Use when deciding whether or what to build, comparing opportunities, turning discovery evidence into a product decision, planning validation, or judging readiness to hand off. Do not use for research summaries without a decision, project management, detailed interaction patterns, standalone usability reviews, copy refinement, or standalone technical architecture and implementation.
---

# Before We Make a Mess

## Resolve the execution profile

Resolve this before loading references, inspecting artifacts, or routing work:

- **create:** produce a new discovery frame, decision gate, learning plan, or bounded handoff; write only when the task authorizes it;
- **change:** revise a named discovery artifact or decision record within scope, but write only with separate task-supplied authorization;
- **review:** examine supplied discovery evidence, assumptions, or readiness without modifying artifacts;
- **verify:** test only declared decision-gate conditions or evidence claims on completed work; always remain read-only.

Choose the profile from an explicit token after the skill name, then an explicit handoff `Mode`, then unambiguous request language, otherwise use the existing discovery behavior. A profile never grants write authority.

After resolving any profile, require a concrete task or decision question, usable scope or artifact, and any authority the profile needs. If the request or workflow handoff supplies only the skill name, profile token, or `Mode` without that task context, and no usable recent context resolves it, return only the resolved `Mode` or `Mode: unresolved`, `Status: NEEDS_TASK`, the missing task fields, and `Mutations: none`; then stop before inspecting artifacts, loading references, or routing work.

For a workflow `verify` handoff, require `Question`, `Scope`, `Baseline`, `Criteria`, `Authority: read-only`, `Locked Decisions`, `Invocation ID`, `Artifact Revision`, and `Pass Limit: 1`. A direct conversational invocation may recover the artifact, closed question, scope, baseline, and criteria from the immediately preceding context only when one interpretation is strongly supported. Otherwise return only `Mode: verify`, `Status: NEEDS_TASK`, the missing task fields, and `Mutations: none`.

In `verify`, check only the declared conditions and directly relevant evidence in one bounded pass. Load only references required to interpret that evidence. Retry one tool action only for a clearly transient safe failure. Do not mutate files, designs, configuration, or external systems; do not restart discovery, propose a new research program, reprioritize risks, or recommend or execute a learning action; do not invoke another skill; and do not execute a handoff or `Next Task`.

End `verify` with `Mode`, terminal `Status: PASS | FAIL | BLOCKED`, checked `Scope`, criterion-specific `Evidence`, `Failed Criteria`, optional uninvestigated `Out-of-scope Signals`, `Owner` for a failure, and `Mutations: none`. `PASS` needs named evidence for every criterion; use `BLOCKED` when decisive evidence or a required tool is unavailable.

This terminal report replaces the normal discovery output. In `verify`, retain the claim-state, provenance, evidence-limitation, and decision-gate rules below only as needed to judge declared criteria; skip framing, risk prioritization, learning design, recommendations, routing, and handoffs.

## Operating contract

Make an uncertain product decision explicit and evidence-aware before consolidating a UX/UI solution. Produce a decision, a focused learning action, or a bounded handoff—not a delivery roadmap or an encyclopedic checklist.

Never invent users, evidence, metrics, research findings, provenance, or confidence. Keep facts/evidence, inferences, assumptions, and unknowns visibly distinct.

If the request is solely about interaction patterns, interface usability, visible text, project delivery, or technical implementation, route it to the relevant specialist and stop. When discovery and design are mixed, resolve the blocking product decision first and hand off only the remaining responsibility.

## Workflow

1. **Define the decision.** Rewrite the request as a concrete commitment to accept, defer, reframe, or reject. Name whether it concerns an opportunity, candidate solution, learning activity, or readiness gate.
2. **Frame the opportunity.** State target, situation, problem, current alternative, desired outcome, success signal, urgency, and material constraints. Separate the outcome from the proposed solution. Mark missing information rather than filling it plausibly.
3. **Build the claim ledger.** Classify each decisive claim as `evidence`, `inference`, `assumption`, or `unknown`. Preserve provenance, limitations, and contradictions. Treat stakeholder opinions and model output as claims, not evidence.
4. **Prioritize risks.** Translate assumptions into consequences if false. Consider problem/value, use/comprehension, feasibility, business/context, and harm only when they can change the decision. Keep at most five active risks by default.
5. **Choose the next learning action.** Target the highest-priority risk with the smallest credible research activity, experiment, prototype, spike, or bounded live test. Predeclare observable signals and the decision each result would change.
6. **Take a position.** Select `proceed`, `continue discovery`, `reframe/pause`, or `stop`. Explain the evidence used, residual risk, reversibility, and what the state authorizes now. Do not present `proceed` as proof or `stop` as permanent truth.
7. **Define the handoff.** Pass only the problem frame, decisive claims, accepted risks, constraints, prioritized principles, open questions, and review triggers. Do not perform the recipient skill’s work.

Ask a question only when its answer could materially change the next action. Otherwise proceed with explicit assumptions and a conditional recommendation.

## Collaboration handoff

- Accept an optional handoff containing goal, evidence, constraints, decisions, open risks, artifact paths, and one next task; do not require an upstream skill or a fixed pipeline.
- Verify relevant artifacts and treat handoff statements as claims: preserve provenance and keep evidence, inference, assumption, unknown, and prior decision distinct.
- Keep prior decisions as constraints unless new evidence or a blocking contradiction requires them to be reopened; state any reversal explicitly.
- When discovery authorizes downstream work, produce a handoff of at most 400 words using those same fields rather than copying the discovery brief.
- Put only settled product decisions and confidence in `Decisions`; keep unresolved interaction questions and accepted exposure in `Open Risks`.
- Set `Next Task` to one precise responsibility that is now ready. Suggest another installed skill only when that responsibility is outside discovery; otherwise name the capability without making the suite mandatory.

## Reference routing

Load only the references required by the current decision:

- Read [opportunity-framing.md](references/opportunity-framing.md) when the request begins with a feature, vague opportunity, unclear outcome, multiple stakeholders, or unordered product principles. Skip it when the problem frame is already decision-ready.
- Read [evidence-and-risk.md](references/evidence-and-risk.md) when interpreting research or data, checking provenance, separating claim states, resolving contradictions, classifying reversibility, or prioritizing risks. Skip it for a simple framing request with no evidence to assess.
- Read [experiments-and-prototypes.md](references/experiments-and-prototypes.md) when proposing a learning activity, selecting prototype fidelity, protecting participants, or interpreting test results. Skip it when no experiment or result is at issue.
- Read [decision-gates-and-handoffs.md](references/decision-gates-and-handoffs.md) when issuing a go/no-go or readiness decision, recording a commitment, or handing work to interaction design or engineering. Skip it during early framing that does not authorize a transition.

Read more than one reference only when the request genuinely spans those responsibilities. Never load all four by default.

## Decision criteria

Prioritize risks in this order:

1. cost of error, including harm and expensive reversal;
2. power to block downstream decisions;
3. weakness or contradiction of current evidence;
4. urgency of the real decision point;
5. information gained per unit of cost, time, and exposure.

Require stronger evidence for irreversible or difficult-to-reverse commitments. For bounded reversible decisions, allow lighter evidence only with an exposure limit, rollback path, owner, and trigger.

Avoid numeric scoring unless the user supplies a meaningful model. If risks remain tied, explain the trade-off and choose the one that can produce decision-changing learning sooner.

Authorize an interaction-design handoff only when the target, problem, outcome, alternatives, solution boundaries, constraints, decisive evidence, assumptions, critical residual risks, and open interaction questions are explicit enough that design can proceed without hiding a product gap. Do not claim readiness for engineering from discovery evidence alone.

## Output

Title the default response `Discovery decision brief`. Include only useful sections, in this order:

1. **Decision and state**—decision question plus `proceed`, `continue discovery`, `reframe/pause`, or `stop`.
2. **Problem, target, and outcome**—concise frame and material constraints.
3. **Claim ledger**—state, claim, provenance or reasoning, limitation, and decision implication.
4. **Priority risks**—at most five by default, with consequence, evidence gap, and reversibility.
5. **Next learning action**—target risk, minimum method or artifact, participants/data, observable signals, safeguards, and affected decision.
6. **Recommendation**—what to do now, why, and which residual risk is being accepted.
7. **Readiness or handoff**—conditions met, conditions missing, recipient, and review trigger.

Compress simple cases and omit empty sections. If evidence is absent, foreground unknowns and the next learning action. Name user-provided artifacts directly; do not cite the source material behind this skill.

## Quality rules

- Record observations separately from explanations; expose plausible alternative interpretations when they could change the decision.
- State what each piece of evidence or test does **not** establish. Never claim that one favorable test validates a product.
- Prefer behavior and operational outcomes over compliments, hypothetical preference, artifact completion, or stakeholder enthusiasm.
- Match prototype fidelity to the uncertainty being tested; higher fidelity is not stronger evidence by default.
- Refuse deceptive or live tests whose learning value does not justify privacy, safety, financial, accessibility, or trust exposure.
- Keep recommendations prioritized and conditional. Do not hide uncertainty behind generic best practices or fabricated confidence percentages.
- Route only the next unresolved responsibility; do not turn the UX/UI suite into a mandatory pipeline.
- Keep the core workflow tool-independent so it works in Codex and Claude Code.
