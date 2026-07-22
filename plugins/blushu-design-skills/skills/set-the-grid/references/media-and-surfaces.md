# Integrate Media, Surfaces, and Structural Whitespace

Use this reference when images, diagrams, aspect ratios, focal points, captions, full-bleed regions, colored surfaces, insets, or structural whitespace drive layout. Do not use it for generic art direction or aesthetic styling without a structural grid question.

## Contents

- [Inventory media constraints](#inventory-media-constraints)
- [Choose fit and span](#choose-fit-and-span)
- [Preserve focal points and information](#preserve-focal-points-and-information)
- [Coordinate captions](#coordinate-captions)
- [Separate surface and content edges](#separate-surface-and-content-edges)
- [Use whitespace structurally](#use-whitespace-structurally)
- [Handle unstable states](#handle-unstable-states)
- [Verify rendered media](#verify-rendered-media)

## Inventory media constraints

Inspect each representative media family before assigning a shared slot.

Record:

- native aspect ratio and available resolution;
- focal point, subject direction, or irreplaceable information;
- whether cropping is allowed;
- intended hierarchy and minimum useful display size;
- caption, credit, legend, or control ownership;
- transparent, irregular, or cut-out edges;
- background and contrast dependencies;
- alternate sources or art direction already available;
- loading, missing, error, and user-generated variants;
- repetition and density across the page or component.

Treat diagrams, documents, screenshots, product images, portraits, and atmospheric photography differently when their information loss differs.

## Choose fit and span

Map media to a small vocabulary of semantic formats rather than arbitrary coordinates.

| Media condition | Structural response |
| --- | --- |
| Crop-safe atmospheric image | Controlled ratio with focal positioning |
| Portrait or subject-led image | Span and ratio that protect the subject |
| Diagram, document, or screenshot | Contain or preserve native ratio |
| Detail-dependent media | Larger span or dedicated inspection state |
| Repeated gallery items | Governed format set with predictable density |
| Irregular or transparent object | Aligned containing field, not forced crop |
| Media with long caption | Span that supports both image and caption measure |

Use a larger span only when information, hierarchy, or comparison needs it. Do not turn every high-resolution asset into a feature format.

If no common format preserves the content family, allow multiple named variants or separate systems. Do not create one universal crop rule.

## Preserve focal points and information

Choose among crop, contain, alternate source, changed ratio, or grid break.

1. Inspect the subject at every intended mode.
2. Identify the smallest crop that preserves meaning.
3. Check whether focal positioning remains valid as the container changes.
4. Use art-directed sources when one crop cannot serve all modes.
5. Preserve the full frame for diagrams, documents, and evidence-bearing media.
6. Break the standard grid when the information cannot survive its slot.

An intentional grid break must still restore a deliberate relationship: inner alignment, caption ownership, neighboring whitespace, or a documented full-bleed edge.

Do not infer permission to crop from technical possibility. Treat crop rights and content integrity as constraints.

## Coordinate captions

- Keep caption and credit adjacent to the media they describe.
- Give the caption a sustainable measure; do not force it into a narrow residual track.
- Align caption edges with either the medium or a deliberate text line.
- Preserve association when the medium becomes full-width or changes order.
- Include long captions and missing captions in the case matrix.
- Keep visual placement compatible with DOM and reading order.
- Avoid using a detached caption to fill an accidental grid hole.

If caption semantics or wording are unresolved, preserve the structural slot and flag the content dependency.

## Separate surface and content edges

Decide which edge participates in each alignment:

- **surface edge:** background, border, image, or full-bleed region;
- **content edge:** inset text, controls, or nested media;
- **page edge:** outer container or safe-area boundary;
- **track edge:** shared line in the governing grid.

Use nested wrappers when the surface extends beyond the content measure. Keep inset tokens distinct from page margins and track gutters.

For full-bleed treatment:

1. identify the owning container;
2. extend only the surface or medium that needs it;
3. realign meaningful inner content to a documented line;
4. account for safe areas and scrollbars;
5. verify no horizontal overflow;
6. define the compact fallback.

Do not use negative margins as an unexplained correction. If they implement a deliberate bleed, name the primitive and test its bounds.

## Use whitespace structurally

Whitespace can separate, group, delay, or emphasize. Assign it a role rather than distributing leftover space.

Distinguish:

- outer inset protecting the active area;
- gutter separating simultaneous tracks;
- internal inset protecting content inside a surface;
- section gap establishing hierarchy;
- reserved empty field creating emphasis or pacing;
- intrinsic empty space caused by missing content.

Only the first five are design decisions. Detect accidental holes created by incompatible spans, fixed heights, or sparse data.

Reduce whitespace selectively in compact modes. Preserve functional group separation and touch space before preserving wide-mode visual drama.

## Handle unstable states

Test media and surfaces before, during, and after loading.

- Reserve dimensions when layout shift would damage reading or interaction.
- Provide a missing-media state that preserves caption and surrounding structure.
- Check broken URLs, slow sources, transparent assets, and unknown user ratios.
- Avoid fixed heights that clip error or fallback content.
- Verify skeletons and placeholders use the same structural owner as final content.
- Check that background and foreground contrast assumptions survive missing images.

Do not claim performance or accessibility certification. Report layout shift, clipping, order, and visible structural failures within GRID scope.

## Verify rendered media

At compact, regular, wide, and intermediate containers, inspect:

- subject and information integrity;
- crop, contain, and focal behavior;
- image-caption association;
- common edges and intentional breaks;
- whitespace and density around mixed formats;
- full-bleed bounds and inner alignment;
- missing, loading, and error states;
- layout stability as sources resolve;
- zoom and text expansion around captions;
- repeated components with heterogeneous assets.

If one representative image passes but another loses its subject or creates overflow, the media system is not verified.
