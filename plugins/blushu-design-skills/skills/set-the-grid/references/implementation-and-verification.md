# Implement and Verify the Grid System

Use this reference when reviewing or editing code, mapping a grid decision to CSS and tokens, or claiming that a rendered layout is complete. It executes decisions from the other references; it does not re-derive content hierarchy, media policy, or responsive modes.

## Contents

- [Inspect the existing system](#inspect-the-existing-system)
- [Map ownership](#map-ownership)
- [Choose CSS mechanisms](#choose-css-mechanisms)
- [Design semantic tokens and variants](#design-semantic-tokens-and-variants)
- [Implement the smallest coherent change](#implement-the-smallest-coherent-change)
- [Use diagnostics correctly](#use-diagnostics-correctly)
- [Build the verification matrix](#build-the-verification-matrix)
- [Report evidence and failure](#report-evidence-and-failure)

## Inspect the existing system

Before proposing code, locate:

- page shells, containers, layout primitives, and component boundaries;
- existing custom properties, spacing scales, and responsive tokens;
- Grid, Flexbox, block flow, absolute positioning, and table layout;
- media and container queries and their ownership;
- named lines, areas, implicit tracks, subgrids, and nested grids;
- arbitrary offsets, negative margins, fixed heights, and overflow rules;
- duplicated declarations and one-off breakpoint overrides;
- DOM, reading, and focus order;
- tests, stories, screenshots, and visual-regression tools.

Render the current behavior when possible. Do not infer the governing system from class names alone.

Classify findings as:

- **system rule:** shared and intentional;
- **local exception:** justified by a documented content condition;
- **drift:** near-duplicate value or accidental misalignment;
- **compensation:** decoration or offset hiding a structural mismatch;
- **unknown:** behavior that requires rendering or product context.

## Map ownership

Assign each rule to one owner:

| Owner | Examples |
| --- | --- |
| Page shell | global container, page insets, primary regions |
| Template | article, listing, dashboard, or campaign tracks |
| Layout primitive | reusable cluster, stack, sidebar, or frame behavior |
| Component | internal tracks, local container modes, intrinsic sizing |
| Content/media variant | named span, ratio, bleed, or density exception |

Keep a rule at the highest owner that uses it consistently, not the highest possible owner. Do not extend a global grid merely to avoid a local component decision.

When parent and child must share lines, verify that the child truly participates in the parent relationship before choosing subgrid. Otherwise keep the nested system independent.

## Choose CSS mechanisms

Match the mechanism to the relationship:

| Need | Mechanism |
| --- | --- |
| Two-dimensional tracks and spans | CSS Grid |
| One-dimensional distribution or wrapping | Flexbox |
| Content-led document flow | Block or intrinsic layout |
| Flexible track bounds | Intrinsic sizing and `minmax()` |
| Repeated items with intrinsic minimum | Auto-placement with an intrinsic minimum |
| Component response to host width | Container query |
| Page response to viewport or chrome | Media query |
| Child alignment to parent tracks | Subgrid |
| Media ratio and focal control | `aspect-ratio`, fit, and position primitives |

Do not add every mechanism available. Choose the smallest set that expresses the approved model and works with the project’s browser support.

Prefer logical properties for inline and block geometry. Preserve source order that works without layout CSS. Avoid absolute positioning for primary flow unless the design explicitly requires overlap and the content bounds are known.

## Design semantic tokens and variants

Create tokens for roles that recur across the system:

- page inset;
- content maximum;
- track gutter;
- component inset;
- section gap;
- compact, regular, and wide layout modes;
- named content spans or regions;
- media ratios or bleed variants when governed.

Use names that describe purpose rather than current measurements. Keep fluid formulas within verified bounds. Do not expose raw start/end coordinates as a public component API when semantic variants cover the real cases.

Before adding a token:

1. identify at least two consumers or one durable system boundary;
2. name the invariant it represents;
3. state where it may vary;
4. remove or migrate near-duplicate local values;
5. verify the change across all consumers.

## Implement the smallest coherent change

1. Preserve approved product, interaction, content, and visual decisions.
2. Reuse established primitives and tokens where they already express the model.
3. Change the governing rule before patching each symptom.
4. Keep page and component ownership explicit.
5. Add only named exceptions with a content condition and fallback.
6. Remove compensating offsets made obsolete by the new rule.
7. Keep unrelated refactors out of scope.
8. Update proportionate tests or stories when the project supports them.

In review mode, do not edit. In implementation mode, reference real files and components and verify the final rendering.

## Use diagnostics correctly

A temporary grid overlay can reveal track edges, gaps, spans, and drift. It cannot prove readability, hierarchy, crop integrity, semantic order, or responsive behavior.

Useful diagnostics include:

- outline page and component containers;
- color page-owned and component-owned grids differently;
- show named lines or areas when tooling supports it;
- inspect computed track sizes and overflow;
- compare token use with local values;
- disable decoration to inspect structural hierarchy;
- inspect DOM and focus order;
- compare before and after at the same content and width.

Remove or disable diagnostics before delivery unless the project intentionally keeps a development-only grid tool.

## Build the verification matrix

Select a reduced but representative matrix from the touched scope.

### Widths

- compact mode;
- regular mode;
- wide mode;
- at least one intermediate width;
- immediately before and after every changed threshold.

### Content and states

- short, typical, and long text;
- localization or expansion proxy;
- intended and fallback fonts;
- sparse, typical, and dense repeated content;
- mixed-ratio media;
- loading, empty, error, and missing-media states;
- long unbreakable values where credible;
- default and increased zoom.

### Structural checks

- no clipping or unintended horizontal overflow;
- readable or scannable measures;
- preserved content hierarchy and grouping;
- intended shared edges and gutters;
- no cumulative vertical drift that harms alignment;
- preserved media subject, caption, and information;
- stable layout as fonts and media load;
- compatible visual, DOM, reading, and focus order;
- no unexplained local overrides or accidental holes.

Run the project’s relevant tests, lint, type checks, stories, or visual regression in proportion to the change. Do not claim a check ran when it did not.

## Report evidence and failure

Separate:

- **observed:** rendered or measured result;
- **inferred:** conclusion supported by observed evidence;
- **assumed:** reversible input not yet verified;
- **unverified:** check that could not run.

For each material finding or change, report the owner, evidence, decision, affected files or components, widths and states checked, and residual risk.

Completion requires current rendered evidence when the environment permits it. If rendering is unavailable, deliver the code or specification with a verification plan and state that visual completion is pending. A clean diff, passing syntax check, or diagnostic overlay alone is not visual proof.
