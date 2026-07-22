# Evidence and risk

Use this reference to classify claims, preserve uncertainty, translate assumptions into risks, and decide what deserves attention first.

## Maintain a claim ledger

Assign exactly one state to each decision-relevant claim:

| State | Meaning | Required annotation |
| --- | --- | --- |
| **Evidence** | An available observation or datum with identifiable provenance | Source, date or period, population/context, and known limitation when available |
| **Inference** | An interpretation derived from evidence | Supporting evidence, reasoning link, and plausible alternative explanation |
| **Assumption** | A claim the decision depends on but has not established | Consequence if false and a way to learn or accept it |
| **Unknown** | Needed information not yet specific enough to test | Why it matters and what would make it answerable |

Record the observation separately from its explanation. “12 of 20 participants abandoned at step 3” can be evidence; “step 3 is confusing” is an inference until supported by behavior or follow-up.

Never treat these as evidence by themselves:

- stakeholder rank, confidence, or repetition;
- model-generated content;
- an invented or ungrounded persona;
- a prototype being completed;
- a plan, forecast, or target;
- absence of complaints without a credible reporting path.

## Check evidence fitness

Judge evidence against the decision rather than assigning a universal score:

1. **Relevance:** does it concern the target, situation, behavior, and decision at hand?
2. **Directness:** was the behavior observed, reported, inferred from a proxy, or predicted?
3. **Provenance:** can the source, collection method, and transformation be inspected?
4. **Coverage:** which segments, cases, periods, or conditions are absent?
5. **Recency:** could product, market, or behavior have changed since collection?
6. **Independence:** do multiple signals add information or repeat the same source?
7. **Decision sensitivity:** could a reasonable alternative interpretation change the action?

Do not reject imperfect evidence automatically. State what it can support and what it cannot.

## Preserve contradictions

When sources disagree:

1. Keep both observations in the ledger.
2. Check whether target, context, timing, or definitions differ.
3. Generate no more than three plausible explanations.
4. Identify which explanation would change the decision.
5. Prefer the smallest discriminating check over averaging the conflict away.

Use `indeterminate` when available evidence cannot distinguish explanations.

## Convert assumptions into risks

Write each risk as:

> If [assumption] is false, then [consequence] threatens [decision or outcome].

Consider these lenses only when material:

- **Problem/value:** the target may not experience the problem strongly enough or prefer the solution.
- **Use/comprehension:** the target may not understand, access, trust, or complete the intended behavior.
- **Feasibility:** technology, capability, time, or cost may prevent the solution from working.
- **Business/context:** channel, economics, policy, operations, or stakeholder constraints may prevent adoption or support.
- **Harm:** privacy, security, accessibility, fairness, safety, or community impact may make proceeding unacceptable.

Avoid a checklist report. Include a lens only if failure would change the decision.

## Classify reversibility

A decision is **reversible** when exposure can be bounded and the team has a credible rollback trigger, path, owner, and time window.

A decision is **irreversible or difficult to reverse** when it can create non-recoverable harm, substantial sunk cost, migration, external promise, lock-in, or long-lived dependency. Name the mechanism; importance alone does not make a decision irreversible.

Require stronger evidence and explicit dissent for harder-to-reverse commitments. Permit lighter evidence for bounded, reversible trials, but record stop conditions before exposure.

## Produce the risk queue

Apply the priority order from `SKILL.md` and keep at most five active risks by default:

| Priority | Risk if assumption is false | Evidence state | Cost of error | Reversibility | Next decision |
| --- | --- | --- | --- | --- | --- |

Move lower-priority items to “watch” rather than expanding the main queue. A risk without a consequence or affected decision is still only a vague concern.
