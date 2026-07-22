# Observational evidence

Use this reference when usability sessions, recordings, transcripts, support evidence, or analytics are available, or when an inferred finding needs a lightweight test. Do not expand a usability review into a full research program.

## Contents

- Classify evidence and extract events
- Form candidate problems and separate signal from noise
- Handle participant suggestions
- Prepare and choose lightweight verification
- Debrief and attach evidence to findings

## Classify evidence before interpreting it

Use these labels consistently:

- **Observed:** a person performed, said, missed, hesitated, failed, or recovered in the supplied evidence.
- **Reported:** a participant, customer, or stakeholder described past behavior or preference.
- **Measured:** a defined event or outcome appears in reliable quantitative data.
- **Inferred:** the reviewer predicts a consequence from the artifact or known constraint.
- **Assumed:** task, audience, context, or intent was not supplied and had to be provisionally set.

Do not convert reported preference into observed usability, or a single observed event into population prevalence. Keep the raw event separate from the proposed cause.

## Extract events from session material

For each task, build a compact event sequence:

1. intended task and starting state;
2. action or interpretation by the participant;
3. interface response;
4. hesitation, deviation, error, or success;
5. recovery path and whether help was required;
6. participant explanation, if probed after the event.

Quote only the minimum phrase needed to preserve meaning. Prefer timestamps or artifact locations to long transcript excerpts.

## Form candidate problems

Group events by likely interface cause, not by participant or screen. A candidate finding must name:

- the interface signal that created or failed to resolve uncertainty;
- the task consequence;
- the evidence class and number of relevant observations;
- competing explanations or missing context;
- whether the person recovered and at what cost.

Keep separate events separate when they require different fixes, even if they occur on the same screen. Merge repeated symptoms when one underlying label, hierarchy, state, or flow defect explains them.

## Distinguish signal from noise

Usually retain:

- an incorrect concept that changes later decisions;
- a sought word or action that is absent or effectively hidden;
- repeated uncertainty at the same decision;
- a task block, severe error, silent failure, or expensive recovery;
- a problem spanning participants, tasks, states, or entry points.

Usually deprioritize or omit:

- aesthetic likes and dislikes without task impact;
- a feature request that has not been tied to a real need or behavior;
- a momentary wrong turn when the person notices, recovers unaided, and remains untroubled;
- facilitator-induced behavior caused by leading questions or premature help;
- domain difficulty that the interface cannot reasonably remove.

Do not discard a single occurrence automatically. One observation can expose a serious deterministic failure, especially in safety, payment, privacy, or irreversible actions.

## Handle participant suggestions

Translate “I want feature X” into the underlying task, obstacle, or desired outcome. Test whether the existing interface already supports it and whether discoverability, terminology, or feedback is the real problem. Preserve the suggestion as reported evidence; do not present the participant's proposed design as the recommendation by default.

## Prepare a lightweight verification

Use a small qualitative test when the purpose is to find and improve problems, not prove prevalence.

- Select the smallest artifact that exposes the disputed interaction.
- Define realistic tasks around outcomes, not interface instructions.
- Include necessary account or scenario information without revealing the expected path.
- Ask the participant to think aloud.
- Avoid teaching, leading, or explaining during the task; ask neutral prompts such as what they are considering.
- Save probing questions until after task behavior is captured.
- Stop when the task finishes, the participant is unproductively stuck, or no new behavior is emerging.

Use domain-representative participants when specialized knowledge changes interpretation. Include people with relevant access needs when evaluating assistive use. Escalate high-risk, quantitative, or compliance questions to appropriate research and specialist methods.

## Choose what to verify

Prioritize hypotheses where:

- the artifact supports multiple plausible interpretations;
- stakeholder disagreement is based on preference;
- a structural change would be expensive;
- reviewer familiarity may hide a novice problem;
- context, device, or entry point strongly affects behavior;
- available evidence conflicts.

Do not test merely to choose colors or settle taste when a more important concept, navigation, or task issue remains unresolved.

## Debrief without inflating certainty

- List observed events before discussing fixes.
- Ask observers for the most serious task problems, not every anomaly.
- Order problems before considering implementation ease.
- Keep minor fixes in a separate list so they do not displace serious issues.
- Record a proposed correction, owner, and verification only after the problem is agreed.
- State what the sessions did not establish.

Use repeated small rounds to improve the artifact. Do not claim statistical significance, universal behavior, or complete problem coverage from qualitative sessions.

## Attach evidence to the final finding

Include:

- `Evidence: observed | reported | measured | inferred`
- source location, session, timestamp, or artifact state;
- concise event and recovery behavior;
- confidence and the reason for uncertainty;
- the next check that could confirm or falsify the interpretation.

If behavior was not observed, use `inferred` even when the heuristic signal appears strong.
