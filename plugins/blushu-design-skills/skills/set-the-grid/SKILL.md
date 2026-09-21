---
name: set-the-grid
description: Design, implement, diagnose, and verify responsive structural layout systems for web pages and components. Use when work requires coordinated decisions about containers, columns, modules, margins, gutters, spans, alignments, vertical rhythm, whitespace, media placement, layout tokens, or structural transformations across viewport and container sizes; also use to repair brittle or inconsistent grids in rendered interfaces. Do not use for product discovery, interaction-pattern selection, purely aesthetic polish, generic usability review, or semantic line breaking.
---

# Set the Grid

## Resolve the execution profile

Resolve this before loading references or inspecting the project or artifact:

- **create:** produce a new structural layout decision, system specification, or verification plan; write only when the task authorizes an artifact;
- **change:** revise or implement an existing structural system within the named scope, but write only with separate task-supplied authorization;
- **review:** inspect a supplied layout for evidence-backed structural problems without modifying files;
- **verify:** test only declared container, span, alignment, threshold, order, overflow, or responsive-transformation criteria on completed work; always remain read-only.

Map the previous `design` mode to `create`, and `revision` or `implementation` to `change`; implementation still requires explicit write authorization. Treat a focused decision as a scope modifier. Choose the profile from an explicit token after the skill name, then an explicit handoff `Mode`, then unambiguous request language, otherwise preserve the existing structural design/review behavior.

After resolving any profile, require a concrete structural task or question, usable scope or artifact, and any authority the profile needs. If the request or workflow handoff supplies only the skill name, profile token, or `Mode` without that task context, and no usable recent context resolves it, return only the resolved `Mode` or `Mode: unresolved`, `Status: NEEDS_TASK`, the missing task fields, and `Mutations: none`; then stop before inspecting artifacts, loading references, or routing work.

For a workflow `verify` handoff, require `Question`, `Scope`, `Baseline`, `Criteria`, `Authority: read-only`, `Locked Decisions`, `Invocation ID`, `Artifact Revision`, and `Pass Limit: 1`. Recover a direct conversational task from the immediately preceding context only when artifact, closed question, scope, baseline, and criteria have one strongly supported interpretation. Otherwise return only `Mode: verify`, `Status: NEEDS_TASK`, the missing fields, and `Mutations: none`.

In `verify`, check only declared criteria and directly affected neighboring state in one bounded pass. Use rendered evidence when geometry or responsive behavior is claimed and load only the references necessary for those criteria. Retry one tool action only for a clearly transient safe failure. Do not mutate files, designs, configuration, or external systems; do not derive a new grid, broaden into structural diagnosis, or recommend or apply a repair; do not invoke another skill; and do not execute a handoff or `Next Task`.

End `verify` with `Mode`, terminal `Status: PASS | FAIL | BLOCKED`, checked `Scope`, criterion-specific `Evidence`, `Failed Criteria`, optional uninvestigated `Out-of-scope Signals`, `Owner` for a failure, and `Mutations: none`. `PASS` needs evidence for every criterion; use `BLOCKED` when decisive rendering, an artifact, or a required tool is unavailable.

This terminal report replaces the normal output. In `verify`, retain only domain evidence, selective reference, rendered-verification, and quality rules needed for declared criteria; skip inventory expansion, candidate derivation, redesign, implementation, recommendations, routing, and handoffs.

## Establish scope and evidence

Identify the target page, template, component family, or layout system; the content hierarchy; the structural problem; and the requested mode.

- Treat `create` without artifact authorization and all `review` requests as read-only.
- Treat build, refactor, implement, or fix language as write authorization only when the current task clearly requests an actual mutation; a `change` profile token alone is never permission.
- Keep product strategy, interaction behavior, aesthetic direction, usability claims, copy, and semantic line breaking outside scope.
- For mixed requests, complete only the structural portion supported by existing decisions and name any required handoff.
- Do not infer grid-system work from a vague request to clean up layout or spacing; require a coordinated structural signal or keep the response to a focused diagnosis.
- Inspect the workspace, current implementation, tokens, handoffs, and rendered evidence before asking for information already available.
- Ask only when missing hierarchy, target containers, or content form would force materially different costly work; otherwise use a reversible labeled assumption.
- Mark evidence as observed, supplied, inferred, assumed, or unverified. Never present placeholder content as evidence.

Choose one operating mode:

- **Create/design:** specify the system and verification plan without editing unless an artifact is explicitly authorized.
- **Change/revision:** diagnose an existing system and propose the smallest coherent correction; edit only with separate authorization.
- **Review:** report prioritized structural findings without editing.
- **Focused decision:** narrow any non-verify profile to one bounded question without expanding into a redesign.
- **Verify:** use only the bounded terminal contract above.

## Execute only the necessary workflow

Run only the steps needed by the scope. For a focused decision, skip unrelated inventory, candidate derivation, transformation, implementation, and reference loading.

### 1. Inspect the current system

Locate governing containers, component boundaries, primitives, tokens, queries, offsets, overflow, media wrappers, and DOM or focus order. Render representative states and widths when possible. Distinguish shared rules, justified exceptions, drift, compensation, and unknown behavior.

### 2. Inventory content and constraints

Record only variables that can change the decision: content hierarchy and variation, density and states, media constraints, fonts, target containers, zoom, browser support, existing primitives, and governance.

### 3. Diagnose the structural failure

Check readable measure, shared edges, granularity, whitespace ownership, vertical drift, arbitrary spans, crop damage, visual versus DOM order, desktop-only geometry, threshold cliffs, nested-grid ownership, and repeated local overrides. Decide whether the issue is systemic or local.

### 4. Derive and choose a system

Start from active container behavior, logical insets, gutters, minimum tracks, vertical relationships, recurring spans, and real content cases. Compare no more than three candidates. Include intrinsic flow, Flexbox, an existing primitive, or no new grid whenever plausible.

Choose the least complex candidate that preserves content and hierarchy, transforms well, fits media, respects DOM order, minimizes exceptions, and remains maintainable. Require observable benefit before adding tracks, nested grids, or subgrid. Reject the other candidates briefly.

### 5. Define structural transformations

Find content failure points instead of adopting device-name presets. Define compact, regular, and wide modes only when distinct arrangements are needed. For each mode state container behavior, insets, tracks, gutters, allowed spans, vertical behavior, media treatment, order, and named exceptions.

Preserve relationships rather than desktop coordinates. State what stacks, changes span, becomes full-bleed, switches to intrinsic flow, gains local grid ownership, or disappears only when semantically optional.

### 6. Map ownership and implement when authorized

Assign each rule to the page shell, template, layout primitive, component, or content/media variant that owns it. Prefer semantic tokens and variants over exposed coordinates. Match the mechanism to the relationship: Grid for two dimensions, Flexbox for one, intrinsic flow when content leads, container queries for host-driven components, media queries for page-wide composition, and subgrid only for real parent-child track participation.

In an authorized `change`, reuse local conventions, change the governing rule before patching symptoms, remove obsolete compensation, keep exceptions named, and avoid unrelated refactors. Update proportionate tests or stories when the project supports them.

### 7. Verify rendered behavior

Verify compact, regular, wide, at least one intermediate width, and both sides of each changed threshold when possible. Exercise content and state extremes, real and fallback fonts, localization, media, unbreakable values, and zoom where relevant.

Check for clipping, horizontal overflow, harmful line measure, broken grouping, unintended edge drift, cumulative vertical drift, crop or caption damage, layout shift, unstable thresholds, incompatible visual/DOM/focus order, and unexplained local overrides.

If rendering cannot run, state exactly what remains unverified. Never treat a code diff, token table, or grid overlay as proof of visual correctness.

## Collaboration handoff

- Accept an optional handoff with goal, evidence, constraints, decisions, open risks, artifact paths, and one next task; verify the referenced implementation and rendering before relying on it.
- Preserve supplied interaction regions, behavioral invariants, semantic and focus order, states, and product decisions. Keep observed facts, inferences, assumptions, unverified claims, and decisions distinct.
- Own container, track, span, gutter, alignment, layout ownership, and responsive geometry; do not reopen behavior or reorder the DOM to satisfy a visual arrangement without new blocking evidence.
- When visual refinement is the next unresolved responsibility, produce a handoff of at most 400 words with grid modes, ownership, tokens, spans, named exceptions, tested widths, DOM and focus constraints, residual risks, and artifact paths.
- Put accepted geometry and transformations in `Decisions`; put untested widths, content extremes, fonts, media, and structural dependencies in `Open Risks`.
- Set `Next Task` to one precise out-of-scope responsibility. Suggest an installed skill only when useful; otherwise name the capability. Do not require an upstream handoff or a fixed pipeline.

## Apply decision priorities

Resolve conflicts in this order:

1. Preserve content, semantic and focus order, zoom behavior, and freedom from clipping or unintended overflow.
2. Maintain readable measure and primary task or content hierarchy.
3. Preserve media information, captions, and stable states.
4. Make transformations work across complete container ranges, including intermediate widths.
5. Minimize exceptions, arbitrary offsets, duplicated tokens, and unclear ownership.
6. Support real density and variation with the fewest useful tracks and span presets.
7. Reuse established design-system primitives and governance.
8. Increase visual variety only after structural integrity and maintainability are secured.

When choices remain equivalent, prefer the simpler, more intrinsic, reversible system. Prefer a local component grid when ownership is local. Adapt or abandon the grid when it damages content, order, media, or operability.

## Route references selectively

Load only the references needed for the current decision:

- Read [grid-derivation.md](references/grid-derivation.md) when designing or replacing a page or template grid, choosing track count and spans, diagnosing granularity, or deciding whether a grid is needed.
- Read [responsive-transformations.md](references/responsive-transformations.md) when the layout crosses viewport or container sizes, wide geometry fails, thresholds must be chosen, or page and component grids interact.
- Read [typography-and-rhythm.md](references/typography-and-rhythm.md) when line measure, rendered font metrics, vertical alignment, localization, zoom, captions, or repeated text modules affect the structure.
- Read [media-and-surfaces.md](references/media-and-surfaces.md) when images, diagrams, aspect ratios, focal points, captions, colored surfaces, insets, full bleed, or structural whitespace drive the decision.
- Read [implementation-and-verification.md](references/implementation-and-verification.md) when inspecting or editing code, mapping the model to CSS and tokens, running diagnostics, or claiming rendered completion.

Do not load typography for a media-only problem or media for a text-only problem. For code changes, combine implementation and verification with only the domain references implicated by the artifact.

## Report proportionally

For a focused decision, return the decision, evidence, contraindications, and verification. For a full design, revision, implementation, or review, use only the applicable sections:

```markdown
## Scope
Mode, artifacts, facts, assumptions, target containers, and constraints.

## Diagnosis
Prioritized structural problems and affected content or states.

## Grid decision
Selected model, rejected alternatives, geometry, ownership, spans, and exceptions.

## Responsive transformations
Compact, regular, and wide structural changes.

## CSS and tokens
Mechanisms, semantic primitives, queries, and migration notes.

## Implementation
Files and components changed, only when authorized.

## Verification
Widths, states, content exercised, results, unverified checks, and residual risks.
```

Use concrete measurements only when tied to the inspected implementation and verification; otherwise express relationships or bounded hypotheses. Use a table only when it clarifies transformations or mappings. Name every intentional grid break and its condition. Reference real files and lines for code review or implementation.

Do not claim improved usability, accessibility compliance, or successful visual verification beyond inspected evidence. Finish with targeted handoffs only where a structural decision depends on another discipline.
