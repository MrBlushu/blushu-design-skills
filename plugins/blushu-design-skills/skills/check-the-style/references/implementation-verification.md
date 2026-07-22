# Implementation and verification

Use this reference when the request authorizes changes to code, design files, tokens, or components, or when a proposed refinement must be verified on a real rendering. Preserve the project's stack, conventions, and existing system boundaries.

## Inspect before changing

1. Locate the entry point, affected component, style source, theme, tokens, and shared primitives.
2. Read project guidance and relevant tests before editing.
3. Run or open the existing interface and capture the affected viewport and state when possible.
4. Inspect computed styles and inherited values rather than reasoning only from source declarations.
5. Search for the same component, token, or raw value elsewhere to determine whether the problem is local or systemic.
6. Identify existing variants that already express the required role.

Do not invent a new design system beside an existing one. Do not replace the stack, rewrite unrelated components, or introduce a dependency solely for a visual adjustment without explicit need.

## Implement the smallest systemic change

- Prefer an existing semantic token or component variant.
- When a recurring inconsistency has no suitable primitive, update or add the smallest shared token or variant that expresses the role.
- Change a local value only when the need is genuinely local and document why it should not propagate.
- Migrate one representative instance before broadening a token change.
- Keep responsive behavior attached to the component concern it controls.
- Preserve public APIs and DOM or view structure unless the visual correction truly requires a scoped structural change.
- Avoid arbitrary near-duplicate values, unexplained overrides, and specificity escalation.
- Keep unrelated formatting and user changes intact.

After each coherent change, re-render the affected component before stacking additional polish. If the result does not improve the targeted signal, revert or revise that change rather than compensating with more layers.

## Build a verification matrix

Select cases proportionate to the component, including:

- at least one narrow and one wide representative viewport;
- minimum, typical, and maximum realistic content;
- default plus every interactive state touched by the change;
- empty, loading, error, and populated states when supported;
- supported themes and high-contrast modes affected by the tokens;
- bright, dark, busy, missing, and extreme-ratio media when relevant;
- localization expansion, wrapping, truncation, and large data values when relevant.

Use the same data and viewport for before-and-after comparison. Wait for fonts, images, animations, and asynchronous state to settle before judging the result.

## Check the rendered result

1. Confirm the targeted hierarchy, grouping, readability, state, or media problem changed in the intended direction.
2. Inspect the component in context, not only in isolation.
3. Check neighboring components that consume the changed token or primitive.
4. Look for clipping, overflow, layout shift, stacking errors, lost focus cues, and unintended contrast changes.
5. Exercise keyboard and pointer states visible in the design where the environment permits; do not mistake this for a complete accessibility audit.
6. Review screenshots or visual diffs at comparable dimensions when tooling exists.
7. Run relevant project checks for the files changed, such as type checking, tests, linting, or a production build.

A passing build does not verify the visual result. A plausible source diff does not verify the rendering. Require both code-level checks and rendered evidence when the environment supports them.

## Handle unavailable verification

- Try the project's documented local workflow before introducing new tooling.
- If the application cannot run, inspect static output, existing stories, screenshots, or component previews that are already available.
- If only one viewport or state is available, verify it and list the missing cases explicitly.
- Do not claim “verified,” “fixed,” or “responsive” for cases that were not rendered.
- Separate an implementation defect from an environment, data, font, or asset limitation.
- Provide the exact command, route, viewport, state, or fixture needed for the pending check.

## Report implementation evidence

For each implemented priority, record:

- the observable problem and intended effect;
- the file, component, token, or variant changed;
- whether the change is shared or intentionally local;
- the viewports, states, themes, content extremes, and assets rendered;
- the before-and-after result observed;
- the project checks run and their outcome;
- any remaining risk, unverified case, or handoff.

Keep preference choices distinct from functional corrections and verifiable improvements. Report only the checks actually performed.
