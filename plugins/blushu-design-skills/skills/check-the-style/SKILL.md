---
name: check-the-style
description: Analizza, progetta, implementa e verifica il visual design di interfacce web e mobile. Usa quando una UI esistente o in sviluppo appare debole, rumorosa, incoerente o poco rifinita, oppure quando occorre migliorare gerarchia, spaziatura, tipografia, colore, contrasto, profondità, immagini, stati, resa responsive e token. Non usare come skill primaria per strategia prodotto, pattern di interazione, griglie complete, test di usabilità, copywriting, line composition o audit completi di accessibilità.
---

# Check the Style

## Set scope and mode

Require at least one concrete artifact: code, a runnable interface, URL, screenshot, recording, mockup, exported design, or pasted component. Inspect the project before asking for information already available on disk.

Use available tokens and themes, approved brand assets, target viewports, representative state and content fixtures, accessibility or localization constraints, visual baselines, and prior handoffs. Do not require every optional artifact for a local review; ask only for evidence whose absence would materially change the visual decision.

Infer the operating mode from the request:

- **Review:** inspect without modifying files; return prioritized findings and concrete fixes.
- **Design direction:** propose roles, tokens, variants, or visual decisions; do not apply them without authorization.
- **Implementation:** modify only the authorized code or design scope, preserve the existing stack and system, then verify the rendering.
- **Focused refinement:** address only the requested visual axis and load only its reference.

Treat “review,” “evaluate,” “explain,” and equivalent read-only phrasing as read-only. Treat “fix,” “refine,” “implement,” “apply,” and equivalent direct change requests as permission to edit within the named scope.

Keep product strategy, audience, outcomes, roadmap, interaction-pattern selection, navigation and flow design, full grid-system architecture, usability research, copywriting, semantic line composition, and complete accessibility audits outside scope. Refine the visual representation of already-decided patterns, states, content, and layout.

If the request is wholly outside visual design, do not solve it provisionally. State that the decision is outside this skill, name the appropriate workflow, and stop without proposing a product, interaction, navigation, flow, grid, copy, usability, or compliance solution. For a mixed request, continue only with an independent visual refinement; do not let a local assumption decide the blocked adjacent work.

Route blocking adjacent work precisely:

- route an unclear problem, audience, or outcome to `before-we-make-a-mess`;
- route interaction-pattern, navigation, flow, and behavioral-state choices to `make-it-flow`;
- route a complete column, gutter, module, or breakpoint system to `set-the-grid`;
- route observed comprehension, orientation, or task-friction questions to a dedicated usability review;
- route intentional semantic line breaks to `break-it-right`;
- route copy changes and complete accessibility compliance to their dedicated workflows.

Stop only the blocked portion. When a local and reversible refinement can proceed, state the narrow assumption and continue.

## Run the workflow

1. **Confirm scope.** Identify the artifact, requested outcome, operating mode, available viewports and states, constraints, and assumptions.
2. **Apply the boundary gate.** Separate visual-design work from missing product, interaction, content, grid, usability, or accessibility decisions before loading references.
3. **Inspect before proposing.** Read relevant structure, styles, tokens, themes, and shared components. Observe the real rendering and supported states when executable. Do not invent a parallel design system.
4. **Recover intended priority.** Use established goals and decisions to determine what should be seen first. Make a limited assumption only when the change stays local and reversible.
5. **Diagnose observable signals.** Check in order: lost or illegible content; ambiguous hierarchy or grouping; unstable responsive proportions; systemic inconsistency; depth, media, and states; final polish.
6. **Classify each finding.** Mark it F, V, or P using the criteria below. Keep preference separate from defects and verifiable improvements.
7. **Prioritize.** Select normally three to five interventions by class, task impact, recurrence, evidence, confidence, reversibility, and system reach.
8. **Specify the change.** State the evidence, effect, concrete code or design change, conditions, contraindications, shared-system impact, and expected rendered proof.
9. **Implement only when authorized.** Reuse existing primitives and conventions. Prefer one shared token or component correction to repeated local patches. Avoid unrelated rewrites and arbitrary one-off values.
10. **Verify the result.** Compare before and after on real rendering. Check at least one narrow and one wide viewport when possible, the states touched, and representative content extremes.
11. **Deliver proportionately.** Separate observations, implemented changes, preference choices, verified results, pending checks, and focused handoffs.

## Collaboration handoff

- Accept an optional handoff with goal, evidence, constraints, decisions, open risks, artifact paths, and one next task; inspect the actual artifacts and rendering before relying on it.
- Preserve product, interaction, content, and grid decisions as constraints unless new evidence exposes a blocking conflict. Keep observations, inferences, assumptions, preferences, and decisions distinct.
- Keep visual changes local to the accepted structure: do not change shared tracks, gutters, spans, or breakpoints. Hand repeated structural failures back to grid work with the affected artifacts and states.
- When usability review is the next unresolved responsibility, produce a handoff of at most 400 words with verified visual changes, preserved tradeoffs, covered states and viewports, unverified risks, and artifact paths.
- Put accepted visual roles, tokens, and variants in `Decisions`; put missing render checks and actual text-wrapping signals in `Open Risks` without performing line composition.
- Set `Next Task` to one precise out-of-scope responsibility. Suggest an installed skill only when useful; otherwise name the capability. Do not require an upstream handoff or a fixed pipeline.

## Classify and prioritize

Use these classes consistently:

- **F — functional visual correction:** essential content is unreadable, clipped, hidden, ambiguous, or communicated only through color; an asset is unusable; an overlay or stacking relationship hides a control.
- **V — verifiable visual improvement:** the interface remains usable, but hierarchy, grouping, responsive proportions, token consistency, depth, media treatment, or state representation can be observably improved.
- **P — subjective preference:** personality, ornament, color temperature, decorative style, or an equivalent aesthetic direction depends on taste or an approved brief.

Order findings as follows:

1. F that blocks reading, meaning, access to controls, or content integrity.
2. V with high task impact or repeated system-wide effect.
3. V local to one component without primary-task impact.
4. P, unless the user explicitly asks to explore or apply an aesthetic direction.

At equal class, prefer the finding that affects the primary task, repeats across components, has stronger rendered evidence, supports direct verification, fits the existing system, and creates the least adjacent-scope risk.

Do not call a P choice an error. Do not promote P above F or V without explicit direction.

## Load references selectively

Read only the files required by the observed signal and requested mode:

- Read [hierarchy-spacing.md](references/hierarchy-spacing.md) for visual priority, label or action emphasis, grouping, spacing rhythm, density, intrinsic sizing, or responsive component proportions. Skip it for work limited to palette, elevation, or media.
- Read [typography-color.md](references/typography-color.md) for type roles, measure, line height, baseline or optical alignment, palette roles, contrast, themes, or meaning that relies on color. Skip it for work limited to images or stacking.
- Read [depth-images-states.md](references/depth-images-states.md) for elevation, z-order, surfaces, borders, overlays, icons, screenshots, image contrast, user uploads, media ratios, or the visual treatment of defined empty, loading, error, and populated states. Skip it for a type-scale or spacing-token-only task.
- Read [implementation-verification.md](references/implementation-verification.md) whenever modifying code, design files, tokens, or shared components, or when verifying before/after rendering across viewports, states, themes, content extremes, or media cases. Skip it for a read-only review of one static screenshot with no implementation path.

Load multiple references only when the request genuinely crosses their concerns. Do not read every reference by default.

## Format the output

Use the smallest useful response. Produce fewer than three priorities for a tightly focused issue and normally no more than five.

```markdown
## Scope
Mode, artifacts observed, available viewports and states, constraints, and assumptions.

## Priorities
1. [F|V|P] Short title
   - Evidence: observable signal, not a generic judgment.
   - Effect: impact on hierarchy, readability, perception, or state.
   - Change: concrete decision and file, component, or design scope.
   - System: shared token, variant, primitive, or intentionally local rule.
   - Verification: rendered viewport or state, expected result, and confidence.

## Changes
Files or design artifacts modified, only when authorized.

## Limits
Checks not run, missing evidence, unresolved dependencies, and focused handoffs.
```

Include real file paths and check results after implementation. Omit empty sections when the task does not require them.

## Enforce quality gates

- Ground every finding in an observable artifact; label assumptions and inferences.
- Preserve established product, interaction, content, and grid decisions.
- Prefer system-level corrections only when the evidence repeats; avoid premature design-system rewrites.
- Test narrow and wide viewports, touched states, and realistic content extremes when the environment permits.
- Check affected shared consumers after changing tokens or primitives.
- Correct contrast and color-only meaning without claiming a complete accessibility audit.
- Control font metrics and measure without deciding semantic line breaks or rewriting copy.
- Report an asset limitation instead of hiding an unsuitable source with effects.
- Do not cite source material, page numbers, or design theory in runtime output.
- Do not return an exhaustive aesthetic checklist when a few priorities drive the result.
- Do not claim “verified,” “fixed,” or “responsive” without updated rendered evidence for those cases.
- If rendering is unavailable, state exactly what remains pending and how to verify it.
