# Derive a Grid from Real Content

Use this reference when creating or replacing a page or template grid, choosing track granularity, or governing allowed spans. Do not use it for detailed responsive transformations, typographic rhythm, media art direction, or code verification.

## Contents

- [Start from evidence](#start-from-evidence)
- [Decide whether a grid is needed](#decide-whether-a-grid-is-needed)
- [Derive the active area](#derive-the-active-area)
- [Choose tracks and modules](#choose-tracks-and-modules)
- [Govern alignments and spans](#govern-alignments-and-spans)
- [Compare candidate systems](#compare-candidate-systems)
- [Record the decision](#record-the-decision)

## Start from evidence

Inspect the actual artifact before choosing geometry. Build a compact case matrix with:

- primary, secondary, and supporting content;
- repeated content types and their count ranges;
- shortest and longest credible text;
- dense, typical, and sparse states;
- media formats and caption ownership;
- fixed controls, tables, diagrams, and long unbreakable values;
- page-level versus component-level layout ownership;
- localization, zoom, safe-area, and embedding constraints;
- existing containers, tokens, primitives, and authoring conventions.

Mark each item as observed, supplied, inferred, or assumed. Do not present placeholder content as evidence. If real content is unavailable, choose a reversible provisional model and name the evidence that could invalidate it.

## Decide whether a grid is needed

Choose the simplest sufficient layout mechanism before deriving tracks.

| Situation | Prefer | Reason |
| --- | --- | --- |
| Natural document flow with few shared edges | Block or intrinsic flow | Content already supplies the order and size |
| One-dimensional group or distribution problem | Flexbox | Only one axis needs coordinated layout |
| Repeated items with intrinsic minimums | Auto-fit or intrinsic grid | Items, not named coordinates, determine packing |
| Two-dimensional page relationships | Explicit Grid | Rows, columns, spans, and shared edges interact |
| Descendants must share parent tracks | Subgrid candidate | Cross-boundary alignment is real and stable |
| One component has an independent internal system | Nested grid | Ownership is local rather than inherited |

Reject a new grid when it adds coordinates without reducing exceptions, clarifying hierarchy, or improving reuse.

## Derive the active area

1. Render the real font and representative content.
2. Establish the useful reading or working measure for the primary content.
3. Identify elements that legitimately need wider or narrower measures.
4. Define outer container behavior and logical page insets.
5. Separate outer margins, track gutters, component insets, and section gaps; do not use one token for all four roles.
6. Check safe areas, embedded contexts, scrollbars, and full-bleed requirements.

Treat values as relationships first:

- container width follows content and context, not a device preset;
- margins protect the active area and may vary by mode;
- gutters separate simultaneous tracks and follow density needs;
- section gaps express hierarchy rather than compensating for weak grouping;
- internal insets belong to the surface or component that owns them.

Choose concrete values only after rendering. Record the content or alignment condition each value protects.

## Choose tracks and modules

Start coarse. Add tracks only when a recurring case needs a distinct span or shared edge.

1. List the minimum set of required content widths and combinations.
2. Propose the smallest track count that can express them.
3. Map each recurring case to an allowed span.
4. Add a subdivision only when it removes repeated exceptions or enables a valuable recurring format.
5. Re-run the case matrix after every increase in granularity.

Evaluate granularity with observable signals:

| Too coarse | Sufficient | Too fine |
| --- | --- | --- |
| recurring one-off widths | cases map to a small span vocabulary | authors select arbitrary coordinates |
| forced crops or unreadable text | content extremes fit without distortion | many mathematically possible spans remain unused |
| local nested grids repeat the same fix | exceptions are rare and named | CSS needs frequent start/end overrides |
| hierarchy cannot be expressed structurally | span differences stay legible | related pages drift despite sharing tracks |

Do not preserve one track count across all containers. Responsive ownership belongs in `responsive-transformations.md`.

## Govern alignments and spans

Name semantic roles instead of exposing raw coordinates whenever the system will be reused.

- Define a small vocabulary such as `content`, `feature`, `wide`, `full`, `aside`, or domain-specific equivalents.
- State which edges align across primary text, secondary text, media, captions, and repeated components.
- Reserve controlled displacement for emphasis; do not let every item invent an offset.
- Keep visual order compatible with document, reading, and focus order.
- Distinguish page-owned lines from component-owned lines.
- Use subgrid only when a child genuinely participates in parent track sizing and alignment.
- Allow an exception only when it protects content, meaning, media integrity, or task structure.

For every exception, record its owner, condition, fallback, and verification. If exceptions become a second undocumented system, revise the grid.

## Compare candidate systems

Build no more than three candidates, including a simpler option when plausible. Populate each with the same case matrix.

Score qualitatively on:

1. content integrity and readable measures;
2. hierarchy and shared-edge clarity;
3. number and severity of exceptions;
4. compatibility with semantic and focus order;
5. reuse across real templates or components;
6. authoring clarity and maintenance cost;
7. ability to transform without preserving desktop coordinates;
8. fit with existing primitives and browser constraints.

Reject candidates explicitly. Choose the least complex candidate that covers the evidence, not the one with the largest theoretical range.

## Record the decision

Capture:

- evidence and assumptions;
- container and inset behavior;
- tracks, gutters, vertical relationships, and named lines or areas;
- allowed semantic spans and forbidden combinations;
- page versus component ownership;
- intentional exceptions and abandon-grid conditions;
- rejected candidates with one-line reasons;
- references to the responsive, typography, media, and verification decisions still required.

The decision is incomplete if a future implementer must infer which content case justified the geometry.
