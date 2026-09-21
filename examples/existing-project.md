# Existing Project Requests

Use a specialist directly when the project already exists and the problem does not require an end-to-end website workflow.

## Choose an Execution Profile

Use `review` for open diagnosis, `change` for an explicitly authorized modification, and `verify` for a closed read-only regression check.

### Open review

```text
Use make-it-obvious review on ./src/preferences.html.
Review the task of changing and saving notification preferences.
Prioritize evidence-backed usability problems and define verification criteria.
Do not modify files.
```

### Authorized change

```text
Use make-it-obvious change on ./src/preferences.html.
Implement only the accepted fixes U1 and U2 from ./review.md.
You are authorized to edit that file and its directly related tests.
Preserve all other decisions, then report the affected checks.
```

### Closed verification

```text
Use make-it-obvious verify.
Verify only U1 and U2 from ./acceptance-criteria.md against
./src/preferences.html at its default state.
This is read-only: do not fix failures, expand into a general review, invoke
another skill, or execute a handoff. Return PASS, FAIL, or BLOCKED with evidence,
failed criteria, owner when relevant, and Mutations: none.
```

If the artifact, question, baseline, or criteria are missing, `verify` returns `NEEDS_TASK` instead of reconstructing intent or starting a review.

## Product Discovery: `before-we-make-a-mess`

```text
Use before-we-make-a-mess to review the proposed account-sharing feature in this existing product.
Inspect the available brief and research notes.
Define the decision, separate evidence from assumptions and unknowns, identify the highest-risk belief, and recommend a focused validation gate.
Do not design screens or create a delivery roadmap.
```

## Interaction Design: `make-it-flow`

```text
Use make-it-flow to review the current search-to-detail flow.
Compare plausible interaction patterns for narrow and wide screens, preserve search state and scroll position, and specify loading, empty, error, retry, and back-navigation behavior.
Implement only if the current request explicitly authorizes code changes.
```

## Responsive Grid: `set-the-grid`

```text
Use set-the-grid to diagnose the current catalog and detail layouts.
Define container behavior, tracks, gutters, spans, alignment ownership, media treatment, and responsive transformations for representative narrow, medium, and wide widths.
Verify the rendered geometry and report exceptions instead of adding page-specific patches.
```

## Visual Design: `check-the-style`

```text
Use check-the-style on the rendered dashboard.
Prioritize hierarchy, spacing, typography, color roles, contrast, imagery, depth, and component-state consistency.
Preserve the accepted navigation, interaction model, grid, and content.
Show which findings are visible evidence and verify any implemented change across representative states and viewports.
```

## Usability Review: `make-it-obvious`

```text
Use make-it-obvious to review the current checkout task from cart to confirmation.
Check comprehension, orientation, action clarity, form friction, error recovery, and loss of entered data.
Separate supplied observations, visible interface signals, and inferred user consequences.
Prioritize the smallest causal fixes and define an observable verification for each one.
```

## Text Composition: `break-it-right`

```text
Use break-it-right on the approved hero, section headings, card titles, calls to action, and navigation labels.
Render the real font at the supported viewport widths.
Compare natural wrapping, width adjustments, and intentional semantic breaks.
Do not rewrite approved meaning or claim success without rendered evidence.
```
