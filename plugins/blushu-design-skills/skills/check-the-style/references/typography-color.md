# Typography and color

Use this reference for type roles, measure, line height, baseline and optical alignment, palettes, contrast, and meaning carried by color. Work with the fonts, color format, accessibility standard, and theme architecture already used by the project.

## Consolidate typography by role

1. Inventory computed font family, size, weight, line height, letter spacing, and color for representative components.
2. Group values by semantic role: display, heading, body, label, metadata, control, code, or other project-specific roles.
3. Find nearly duplicated values that create no perceptible or semantic distinction.
4. Propose a restricted scale whose steps are visible in the actual font, then map roles to it.
5. Migrate one representative component and render it before extending the change.
6. Preserve intentional editorial or data-display exceptions and document why they remain.

Do not invent a complete typography system when a suitable one already exists. Prefer an existing token or variant to a new one-off value. A prototype still exploring visual direction may need looser values until roles stabilize.

## Tune reading and alignment

- Evaluate measure with real content at narrow and wide viewports. Constrain overly long lines without forcing every text block to the same width.
- Set line height from the font, size, measure, and content density. Smaller or longer body text often needs more breathing room than large compact headings.
- Check cap height, x-height, ascenders, descenders, and wrapping in the actual font rather than transferring numeric rules from another typeface.
- Align mixed text sizes, icons, and values by a meaningful baseline or optical relationship. Do not assume geometric centering will look aligned.
- Keep labels and metadata readable after reducing their emphasis.
- Preserve link and action discoverability across default, hover, focus, visited, disabled, and high-contrast variants supported by the product.
- Test localized strings, large values, empty values, and several lines of content when those cases exist.

This skill may control font metrics, width, and line height. Route intentional semantic line breaks in visible copy to the semantic line-composition specialist, and route rewriting or shortening the words to content design.

## Build color around roles

1. Inventory colors from computed styles, tokens, theme files, and component variants.
2. Identify their jobs: text, muted text, surface, border, action, focus, selection, success, warning, danger, information, overlay, or decoration.
3. Find almost-identical values that serve the same job and single values overloaded across incompatible jobs.
4. Build or refine perceptually distinct steps in the color format supported by the project. Do not require a specific color model or a fixed number of shades.
5. Map components to semantic roles instead of page names or raw color names when the existing architecture supports it.
6. Migrate a representative component and inspect all supported themes before broad adoption.

Color temperature, saturation style, and decorative accents are preferences unless the approved brand direction makes them constraints. Present them as alternatives, not objective defects.

## Preserve contrast and meaning

- Check contrast using the current project standard and the rendered foreground, background, opacity, overlay, and state—not isolated swatches alone.
- Treat unreadable text, controls that disappear, and state meaning available only through color as functional visual problems.
- Add a redundant cue such as text, icon, shape, pattern, position, or luminance difference when color carries status or selection.
- Confirm that muted content remains readable and that increasing contrast does not accidentally promote secondary content above primary content.
- Test focus, hover, active, disabled, selected, validation, and feedback states that use the changed roles.
- Inspect light, dark, high-contrast, and branded themes that the product actually supports.
- Do not claim complete accessibility conformance from these checks. Identify semantic, keyboard, assistive-technology, motion, and broader audit work that remains outside scope.

## Reject misleading fixes

- Do not create extra type roles to match every individual text instance.
- Do not reduce font size or contrast simply to make secondary content feel quieter.
- Do not force a single line when wrapping preserves meaning and the component can accommodate it.
- Do not use letter spacing as a general repair for an unsuitable font size or weight.
- Do not align mixed content by arbitrary pixel offsets before checking baseline and font metrics.
- Do not multiply shades without a real semantic or component need.
- Do not rename raw colors as semantic tokens while their usage still mixes incompatible meanings.
- Do not make disabled content indistinguishable from unavailable or missing content.
- Do not use a brand accent for status when the same accent already means action or selection.

When several variants meet readability and role requirements, treat the remaining aesthetic choice as preference and follow the approved brand direction.

Escalate unresolved role conflicts instead of hiding them through weaker text or ambiguous color.

## Verify the refinement

Render representative components at a narrow and a wide viewport when possible. Use real fonts and content, wait for web fonts to load, and compare the same states before and after.

Confirm that:

- text roles form a stable hierarchy without unnecessary variants;
- line length and line height support reading at both viewports;
- wrapping, truncation, and localization expansion do not hide essential content;
- mixed text and icons align consistently across repeated components;
- links and actions remain discoverable without relying on color alone;
- semantic colors keep their meaning in every supported theme;
- contrast is measured or inspected in the final rendered composition;
- token changes improve more than one instance without causing unrelated regressions.

Report the changed role or token, the components and themes inspected, and any unresolved contrast or content dependency. If the actual font, theme, or rendering cannot be tested, mark verification as pending.
