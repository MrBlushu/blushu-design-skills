# Coordinate Typography and Vertical Rhythm

Use this reference when line measure, wrapping, font metrics, captions, localization, zoom, or vertical drift affects the grid. This reference governs structural relationships, not typeface selection, visual styling, copywriting, or semantic line breaking.

## Contents

- [Render before measuring](#render-before-measuring)
- [Set sustainable measures](#set-sustainable-measures)
- [Build flexible vertical relationships](#build-flexible-vertical-relationships)
- [Coordinate text roles](#coordinate-text-roles)
- [Handle repeated components](#handle-repeated-components)
- [Stress text variability](#stress-text-variability)
- [Verify rhythm](#verify-rhythm)

## Render before measuring

Use actual font files and browser rendering whenever possible. Font family, weight, size, line-height, language, fallback, and shaping all affect the geometry.

Before fixing tracks or vertical intervals:

1. wait for the intended fonts to load;
2. record the fallback path and observe its metrics;
3. render representative short, typical, and long content;
4. include headings, body, labels, captions, data, and controls that share the layout;
5. test the supported languages or a credible length proxy;
6. inspect zoom and text scaling rather than assuming nominal CSS pixels remain fixed.

Do not derive a grid from design-tool text boxes or placeholders and then treat browser wrapping as a defect.

## Set sustainable measures

Choose measure from the content role and rendered text, not a universal character count.

Evaluate:

- scan or reading purpose;
- type metrics and line-height;
- expected word length and language;
- density and comparison needs;
- neighboring media, data, or controls;
- the cost of wrapping labels and values;
- the available container range.

Distinguish measures by role when needed. Long-form prose, compact metadata, table values, and display headings do not require the same track width.

If a track works only with shortened copy, determine whether the problem is editorial or geometric. Do not use semantic line composition to conceal an unsuitable column.

## Build flexible vertical relationships

Derive recurring intervals from rendered line-height and meaningful content relationships. Use a small spacing vocabulary, but keep variable content intrinsic.

Prefer:

- content-sized rows for text that can wrap;
- spacing tokens linked to grouping and hierarchy;
- row gaps that preserve separation without forcing equal heights;
- alignment of meaningful starts, ends, captions, or repeated boundaries;
- looser vertical coupling when compact widths produce more wrapping.

Avoid:

- fixed text heights;
- clipping or line clamping used only to preserve alignment;
- equal-card heights that create large empty holes or hide content;
- universal baseline coincidence across unrelated roles;
- theoretical font metrics as proof of rendered alignment;
- margins that encode a second undocumented rhythm system.

A baseline relationship is useful only when it survives real content and improves a repeated alignment. Relax it when it conflicts with localization, zoom, or intrinsic height.

## Coordinate text roles

For every recurring role, record:

| Role property | Structural question |
| --- | --- |
| Measure | Which track or span protects readable or scannable width? |
| Start edge | Which content must share a leading alignment? |
| Vertical interval | Which preceding role establishes its separation? |
| Wrapping | What is the credible minimum and maximum line count? |
| Overflow | Can it wrap, scroll, expand, or require content intervention? |
| Responsive change | Does measure, span, or grouping change by container? |
| Ownership | Does the page or component own the rule? |

Keep hierarchy compatible with document structure. If a visual alignment requires a heading or label to leave its semantic owner, revise the layout.

## Handle repeated components

Choose alignment deliberately instead of defaulting to equal height.

- Align repeated starts when comparison benefits.
- Align actions only when content extremes still fit without hidden truncation.
- Let cards grow independently when preserving content matters more than row edges.
- Use subgrid when repeated descendants must share parent tracks and content participates in sizing.
- Use a component-owned grid when internal roles repeat independently of the page.
- Separate dense and spacious variants semantically; do not expose arbitrary row coordinates.

Test missing fields, extra metadata, validation messages, badges, translated labels, and asynchronous states. A repeated component is not verified with one ideal item.

## Stress text variability

Build a minimal matrix:

1. shortest credible content;
2. typical content;
3. longest credible content;
4. alternate language or expansion proxy;
5. long unbreakable token, URL, identifier, or number;
6. intended font and fallback font;
7. default zoom and increased zoom;
8. empty, loading, error, and populated states where text differs.

Observe wrap count, overflow, orphaned labels, separated units, rhythm drift, and changes in neighboring media or controls.

Hand off copy decisions when the content itself is invalid. Keep the grid responsible for credible variation, not impossible strings with no product rule.

## Verify rhythm

Render compact, regular, wide, and intermediate containers after fonts settle.

Check:

- primary measures remain useful;
- no text is clipped or hidden to protect geometry;
- hierarchy remains clear without relying on decoration alone;
- repeated starts, captions, and actions align where the decision requires them;
- vertical drift does not accumulate across long pages;
- spacing roles remain distinguishable;
- fallback fonts and zoom do not collapse groups or create overlap;
- DOM and focus order remain coherent after any responsive repositioning.

Report observed rendering separately from inferred quality. If line breaks must be curated semantically after the measure is stable, hand off to `break-it-right` rather than encoding specific breaks into the grid.
