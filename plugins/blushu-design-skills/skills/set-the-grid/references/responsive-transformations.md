# Transform Grid Relationships Responsively

Use this reference when a layout changes across viewport or container sizes, when desktop geometry fails at narrower widths, or when page and component grids interact. Derive the base grid first with `grid-derivation.md`.

## Contents

- [Find content failure points](#find-content-failure-points)
- [Assign responsive ownership](#assign-responsive-ownership)
- [Separate invariants from transformations](#separate-invariants-from-transformations)
- [Specify layout modes](#specify-layout-modes)
- [Apply structural transformation patterns](#apply-structural-transformation-patterns)
- [Protect semantic order](#protect-semantic-order)
- [Verify transitions](#verify-transitions)

## Find content failure points

Do not begin with conventional device labels. Resize the real composition and identify the first width where a protected relationship fails.

Look for:

- primary text becoming too narrow or excessively long;
- simultaneous columns losing useful content space;
- controls wrapping into ambiguous groups;
- media crops losing the subject or information;
- captions separating from their media;
- repeated components becoming illegible or uneven;
- whitespace collapsing until groups merge;
- navigation or interaction regions requiring a behavioral redesign;
- horizontal overflow, clipped values, or unstable scrollbar behavior;
- visual order diverging from reading or focus order.

Place a structural threshold where a different arrangement solves the failure. Do not create a threshold merely because a common device width exists.

## Assign responsive ownership

Choose the query mechanism from the owner of the decision.

| Decision owner | Prefer | Typical use |
| --- | --- | --- |
| Page or viewport composition | Media query | Site shell, global navigation, page-wide regions |
| Reusable component in variable hosts | Container query | Card groups, side panels, embedded modules |
| Content size without a discrete mode | Intrinsic sizing or fluid range | Measures, gaps, and tracks that can interpolate safely |
| Parent-child shared alignment | Subgrid plus parent mode | Repeated children that must inherit parent tracks |

Avoid viewport queries inside reusable components when the component can appear in containers of different widths. Avoid container queries when the decision depends on viewport chrome, safe area, or global page composition.

## Separate invariants from transformations

List what must remain recognizable before deciding what can change.

Possible invariants:

- content and task priority;
- semantic, reading, and focus order;
- caption ownership and media information;
- shared design-system spacing roles;
- a small set of recurring alignment relationships;
- component API semantics;
- minimum readable and operable sizes.

Possible transformations:

- track count and track sizing;
- simultaneous versus stacked regions;
- span vocabulary;
- margin and gutter scale;
- full-bleed versus contained media;
- nested-grid activation;
- vertical spacing multiple;
- crop, aspect ratio, or art direction;
- visibility of genuinely optional supporting content.

Preserve relationships, not coordinates. A wide feature span may become earlier source-order emphasis or stronger vertical separation in a compact mode.

## Specify layout modes

Use as many modes as real failures require, usually compact, regular, and wide. A mode is a coherent structural state, not a named screenshot.

For each mode, record:

| Field | Required decision |
| --- | --- |
| Trigger | Content failure or recovery condition |
| Container | Width behavior and logical insets |
| Tracks | Count, sizing model, and ownership |
| Gutters | Role and scaling behavior |
| Spans | Allowed semantic variants |
| Order | Source, reading, visual, and focus compatibility |
| Vertical behavior | Stack, rhythm, and section separation |
| Media | Ratio, crop, focal point, contained/full-bleed state |
| Exceptions | Condition, owner, and fallback |

Prefer adjacent-mode rules that remain stable through the interval. Do not tune only the exact evaluation widths.

## Apply structural transformation patterns

### Reduce simultaneity

Stack secondary regions when each column can no longer preserve useful measure. Keep related content adjacent and retain priority through order and spacing.

### Change the span vocabulary

Replace wide-mode spans with a smaller compact set. Do not simulate missing tracks with fractional offsets or negative margins.

### Promote intrinsic flow

Let variable-height text, lists, and controls size naturally when fixed row relationships would clip or create large holes.

### Switch grid ownership

Allow a component to adopt its own container-driven grid when the page grid no longer describes its internal content. Keep shared tokens without forcing shared coordinates.

### Use full bleed with inner alignment

Let a surface or medium reach the container edge while its meaningful content realigns to the page inset. Verify that no horizontal overflow or safe-area conflict appears.

### Change media treatment

Select an alternate source, crop, ratio, or contained presentation when the original composition loses information. Consult `media-and-surfaces.md` for the decision.

### Abandon the wide grid

Replace rather than compress it when readable measure, touch space, semantic order, or media integrity cannot survive.

## Protect semantic order

- Start with source order that works in the most linear presentation.
- Use visual reordering only when meaning, reading, and keyboard sequence remain compatible.
- Never use CSS `order` to hide an interaction or information-architecture problem.
- Keep headings before the content they introduce.
- Keep captions associated with their media in the accessibility tree and visual flow.
- Verify focus movement after any layout-driven relocation or conditional visibility.
- Hand off to interaction design if the compact mode requires a different behavior, navigation model, or state machine.

## Verify transitions

Render every mode plus widths immediately before and after each structural threshold. Add at least one midpoint between thresholds.

Exercise:

- real and fallback fonts;
- short, long, localized, and unbreakable text;
- sparse, typical, and dense repeated content;
- mixed media, missing media, and loading states;
- zoom and browser text scaling where relevant;
- embedded and full-page containers;
- keyboard focus order and scrolling.

Pass only when no interval shows clipping, accidental overlap, orphaned captions, collapsed grouping, unstable hierarchy, harmful crop, or unexplained override. If the composition works only at named widths, the transformation is not finished.
