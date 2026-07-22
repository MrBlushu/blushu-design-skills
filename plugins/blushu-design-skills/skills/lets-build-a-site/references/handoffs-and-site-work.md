# Handoffs and `.site-work` artifacts

## Maintain compact sources of truth

Create these files outside the skill folder in the active project:

```text
.site-work/
├── site-brief.md
├── asset-manifest.md
├── content-gaps.md
├── site-map.md
├── design-decisions.md
├── ux-product-handoff.md
└── qa-report.md
```

Update them incrementally. Link to project assets instead of copying binary or long source content. Remove stale decisions by marking them superseded with a reason; do not silently rewrite history that a later stage depends on.

## `site-brief.md`

Record:

- working directory and editable scope;
- goal, audience, primary task/CTA, and success criteria;
- separate goal, architecture, and deliverable decisions with confidence;
- factual sources, assumptions, constraints, and non-goals;
- blocking and accepted risks;
- completion criteria specific to the project.

## `asset-manifest.md` and `content-gaps.md`

Use the schemas in `assets-and-content-gaps.md`. Keep paths relative when they remain unambiguous. Make every placeholder traceable to a gap and every excluded material traceable to a reason.

## `site-map.md`

Record each route or section, user intent/question, source content, CTA, relationship, and shared template. Include global navigation, footer/legal destinations, and error routes when applicable.

## `design-decisions.md`

For each durable decision record:

`ID | Owner | Decision | Evidence/reason | Confidence | Rejected alternative | Reopen when`

Also record every specialist as `used` or `skipped` with a concrete reason. Keep interaction, grid, visual, and line-composition ownership distinct.

## `ux-product-handoff.md`

Keep the current handoff under 400 words and include only:

1. **Goal** — outcome and task.
2. **Evidence** — facts/observations with provenance; inferences, assumptions, and unknowns labeled separately.
3. **Constraints** — product, content, technology, platform, accessibility, and non-negotiable limits.
4. **Decisions** — accepted decisions, confidence, and what must not be reopened without evidence.
5. **Open Risks** — unresolved risks relevant to the next owner.
6. **Artifacts** — paths plus relevant viewport, state, route, or fixture.
7. **Next Task** — one owner and one precise question.

Replace the working handoff when responsibility changes; durable decisions stay in `design-decisions.md`.

At final closeout, refresh the handoff after QA. Do not leave a stale `Next Task` such as implementation or QA when it has already finished. Point to the next unresolved approval, external action, or evidence need; if none remains, state that orchestration is complete.

## `qa-report.md`

Record environment, commands, representative routes/templates, viewport/state matrix, and checks as `pass`, `fail`, `not verified`, or `not applicable`. For each failure include symptom, owner, correction, and regression result. Separate automated evidence, static inspection, rendered inspection, and human behavior.

End with blockers, approvals needed, placeholders, mocks/disconnected integrations, and residual risks.

## Final delivery format

Open with the deliverable status, then provide:

1. **Deliverable** — absolute project path and what was built.
2. **Run/verify** — minimal commands.
3. **Architecture** — goal, single/multi-page, deliverable, and brief rationale.
4. **Coverage** — routes/templates, supported widths, interactions, and completed gates.
5. **Specialist routing** — skills used in order and skipped skills with reasons.
6. **Approvals needed** — placeholders, content, integration, or external action requiring confirmation.
7. **Residual risks** — concrete unverified limits only.

Link `site-brief.md`, `site-map.md`, `design-decisions.md`, and `qa-report.md` instead of repeating them.
