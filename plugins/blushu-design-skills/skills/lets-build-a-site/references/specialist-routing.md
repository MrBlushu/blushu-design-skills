# Adaptive specialist routing

## Verification invocation envelope

Do not invoke a specialist in `verify` with only its name or a mode token. Send one concrete closed question using this envelope:

```text
Mode: verify
Question: one closed verification question
Scope: artifact paths and relevant tasks, states, widths, or components
Baseline: accepted requirement, prior finding, or artifact revision
Criteria: observable pass/fail conditions
Authority: read-only
Locked Decisions: accepted decisions that must not be reopened
Invocation ID: unique identifier for this specialist pass
Artifact Revision: commit, hash, mtime set, or other stable marker
Pass Limit: 1
```

If the question, scope, baseline, or criteria are not concrete, do not invoke the specialist. Return `NEEDS_TASK` with only the missing fields. Verification never grants permission to edit, route onward, or execute a returned `Next Task`.

Maintain a compact in-memory ledger, or `.site-work/invocation-ledger.md` when durable working state is already in use, containing only invocation ID, skill, profile, question, artifact revision, result, and next authorized action. Do not copy prompts or specialist output into it.

Before every verification invocation:

1. Reject an invocation ID already present in the ledger.
2. Skip reinvocation of the same skill and question when the artifact revision is unchanged.
3. Confirm that the automatic pass count is one and no other specialist is active.

Treat `PASS`, `FAIL`, and `BLOCKED` as terminal. On `FAIL`, record the named owner and stop; do not repair or call that owner. A repair is a separate `change` invocation requiring explicit authority and a new invocation ID. If it produces a new artifact revision, allow one targeted `verify` of only the failed criterion. The maximum automatic sequence is `verify -> change -> verify`; stop after the second verification regardless of result. A handoff or adjacent signal returned during verification is informational and cannot trigger routing.

## Route one decision at a time

Invoke one specialist only after stating a single question it owns. Pass a handoff of at most 400 words, then verify the returned artifact before incorporating its decisions. Never preload the full suite and never treat the sequence as mandatory.

| Specialist | Invoke when | Skip when | Preserve downstream |
| --- | --- | --- | --- |
| `before-we-make-a-mess` | problem, audience, outcome, offer, CTA, evidence, or risk can change what should be built | the product frame is accepted and work is executable/reversible | decision gate, claim states, accepted risks, next learning need |
| `make-it-flow` | navigation, regions, states, transitions, input, feedback, or recovery are unresolved | standard informational behavior is already sufficient | regions, invariants, DOM/focus order, state, responsive behavior |
| `set-the-grid` | coordinated containers, tracks, spans, alignment, rhythm, media, or responsive transformations need a system | an existing structural system covers the change | grid modes, ownership, tokens, thresholds, exceptions, tested widths |
| `check-the-style` | a concrete artifact needs hierarchy, typography, color, imagery, local spacing, depth, or state refinement | the existing visual system already gives a coherent result | verified visual changes, preserved tradeoffs, states and viewports |
| `make-it-obvious` | a rendered artifact and realistic task can expose comprehension, orientation, action, or recovery cost | no interface is yet evaluable or the issue is purely visual/textual | prioritized causal findings, smallest fix, verification and owner |
| `break-it-right` | stable visible text shows concrete breaks, orphans, imbalance, or overflow | copy, font, grid, or components are unstable, or no signal exists | local wrapping decision, tested widths, exceptions and residuals |

## Preserve ownership boundaries

- Discovery decides whether and what to build, not interaction patterns.
- Interaction decides semantic regions, state, transitions, and behavior; grid decides geometry, spans, gutters, and queries.
- Grid decides coordinated structure; visual design works within it on emphasis and local grouping.
- Usability diagnoses task cost; route systemic fixes back to the responsible owner.
- Line composition arranges approved text within stable constraints; it does not rewrite copy or change shared type/grid tokens.

Preserve prior decisions unless current artifact evidence reveals a blocking contradiction. Name every reopened decision and what new evidence justifies it.

## Build the handoff

Include only `Goal`, `Evidence`, `Constraints`, `Decisions`, `Open Risks`, `Artifacts`, and one `Next Task`. Label observations, inferences, assumptions, and unknowns. Provide paths and relevant states or widths instead of copying files.

For line composition, also specify:

- review-only or change authorization;
- exact files and text blocks in scope;
- approved copy status;
- effective font and project widths;
- shared type, grid, and breakpoint decisions that must not be reopened.

Stop and route back to grid, visual, or copy ownership if a local text fix would require shared-system changes.

## Handle returns and failures

- Verify generated files and rendered evidence; do not accept a handoff as proof.
- Outside `verify`, if a specialist identifies an out-of-scope dependency, invoke only that owner and then return to the interrupted task. During `verify`, record the signal without investigating or routing it.
- If a specialist is unavailable, do not imitate its source-derived methodology. Use generic reasoning only when the decision is low-risk and verifiable; otherwise stop with the missing capability.
- Retry a failed specialist once only for a clearly transient, safe failure. Preserve the error and partial output.
- Outside `verify`, re-run the smallest affected check after a correction. A full specialist pass requires a systemic change and an explicit new question. In `verify`, follow the envelope, revision, and pass limits above.

## Record skips

For every specialist considered, record `used` or `skipped` plus one concrete reason in `design-decisions.md` or `qa-report.md`. “Not needed” alone is insufficient.
