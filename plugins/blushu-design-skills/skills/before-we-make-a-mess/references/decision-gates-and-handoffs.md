# Decision gates and handoffs

Use this reference to turn discovery work into an explicit commitment, pause, or handoff without imposing a rigid product-development pipeline.

## Contents

- [Select a decision state](#select-a-decision-state)
- [Apply gate principles](#apply-gate-principles)
- [Gate an opportunity into solution discovery](#gate-an-opportunity-into-solution-discovery)
- [Gate discovery into interaction design](#gate-discovery-into-interaction-design)
- [Gate interaction design into engineering](#gate-interaction-design-into-engineering)
- [Create the handoff packet](#create-the-handoff-packet)
- [Route to adjacent skills](#route-to-adjacent-skills)
- [Record the decision](#record-the-decision)

## Select a decision state

Use one state and explain why:

- **Proceed:** current evidence and bounded residual risk justify the next commitment.
- **Continue discovery:** the frame remains credible, but one or more blocking risks need focused learning.
- **Reframe/pause:** problem, target, outcome, or candidate direction needs material revision, or timing prevents a responsible decision.
- **Stop:** evidence or constraints make the opportunity or direction not worth pursuing now.

Do not use `proceed` to mean “proven” or `stop` to mean “false forever.” Record the scope and conditions of the decision.

## Apply gate principles

For every gate:

1. Name the commitment being authorized, not a generic phase.
2. Name the decision maker or owner when known.
3. Present supporting and contradicting evidence.
4. Expose assumptions and unknowns that remain.
5. Match the evidence burden to cost, harm, and reversibility.
6. Record the reason, conditions, and review trigger.
7. Reopen when a trigger occurs; do not defend a stale gate.

A council, ceremony, or approval board is optional. Ownership and a traceable decision are not.

## Gate an opportunity into solution discovery

Proceed when the team can state:

- target and situation;
- problem and current alternative;
- desired outcome and useful success signal;
- why the opportunity matters now;
- relevant organizational advantage and constraints;
- a recommendation supported by available evidence;
- the highest-risk assumptions that discovery must address.

Do not require a preferred interface or complete specification at this gate.

## Gate discovery into interaction design

Proceed when these are explicit:

1. problem, target, and situation of use;
2. observable outcome or success criterion;
3. current alternatives and reason to explore the candidate direction;
4. solution boundaries, constraints, and prioritized product principles;
5. evidence, inferences, assumptions, and material contradictions;
6. critical risks reduced or consciously accepted;
7. decision, owner if known, reversal difficulty, and review conditions;
8. open interaction questions that can be resolved without reopening the product problem.

Allow a conditional handoff when missing items are non-blocking. Continue discovery when interaction design would merely give form to an undefined target, problem, or outcome.

## Gate interaction design into engineering

Do not claim this gate from product discovery alone. Require relevant design and engineering evidence, such as:

- behavioral representation of critical flows and states;
- usability findings for high-risk tasks;
- feasibility evidence under realistic constraints;
- accepted accessibility, privacy, security, operational, and business risks;
- current source of truth and decision history;
- delivery owner and rollback or change strategy where relevant.

Route detailed pattern selection to `make-it-flow` and interface diagnosis to `make-it-obvious`.

## Create the handoff packet

Keep the handoff short and decision-oriented:

- **Decision:** state and authorized commitment.
- **Problem frame:** target, situation, problem, alternative, outcome.
- **Evidence ledger:** decisive evidence, inference, assumption, unknown, and contradiction.
- **Risk posture:** reduced, accepted, watched, and blocking risks.
- **Constraints and principles:** ordered trade-offs the next skill must preserve.
- **Open questions:** only questions owned by the recipient.
- **Review triggers:** evidence, date, threshold, or event that reopens the decision.

Do not copy full research archives into the handoff. Link named artifacts and preserve provenance.

## Route to adjacent skills

| Need | Route | Discovery contribution |
| --- | --- | --- |
| Select or combine interaction patterns | `make-it-flow` | Supply problem frame, constraints, principles, and open behavior questions |
| Diagnose comprehension, orientation, or friction in an interface | `make-it-obvious` | Supply target tasks and product risks; consume findings as evidence |
| Refine visible text and semantic line breaks | `break-it-right` | Supply approved intent, hierarchy, and constraints |
| Plan schedule, staffing, dependencies, or delivery reporting | Project management | Supply the authorized commitment and decision conditions only |
| Resolve architecture or implementation feasibility | Engineering | Supply candidate behavior, constraints, and feasibility question |

Do not invoke every adjacent skill as a pipeline. Route only the next unresolved responsibility.

## Record the decision

Use this minimum record:

```text
Decision:
State: proceed | continue discovery | reframe/pause | stop
Commitment authorized:
Evidence used:
Contradicting evidence:
Assumptions and unknowns:
Residual risks:
Reversibility and rollback:
Owner:
Review trigger:
Next recipient or action:
```

Prefer a conditional decision to false certainty. Conditions must name what is allowed now and what remains prohibited.
