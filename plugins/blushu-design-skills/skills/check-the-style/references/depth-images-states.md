# Depth, images, and states

Use this reference for elevation, surfaces, borders, overlays, images, screenshots, icons, user uploads, and the visual treatment of already-defined interface states. Preserve state behavior, content, actions, and copy decisions.

## Make depth communicate structure

1. Inventory shadows, borders, surface changes, overlays, and z-index relationships in representative components.
2. Identify the semantic levels already needed: base content, raised controls, cards, menus, sticky regions, modals, drag states, or other product-specific layers.
3. Match each treatment to a real stacking or interaction relationship.
4. Consolidate recurring levels into a small set of elevation or surface tokens.
5. Migrate one representative component and inspect it beside adjacent levels before extending the change.

Use surface color, border, overlap, blur, or spacing when the product language is intentionally flat. Do not add shadows merely to make the interface feel more polished. Avoid realistic lighting effects that obscure hierarchy or create conflicting light sources.

Treat a menu, modal, overlay, or dragged element that appears behind the content it controls as a functional visual problem. Treat inconsistent but understandable elevation as a verifiable improvement. Treat decorative shadow character as preference unless the approved direction defines it.

## Check interactive layers

- Verify default, hover, focus, active, pressed, selected, disabled, open, dragged, and modal states that use depth.
- Confirm that borders and shadows do not disappear against supported surfaces or themes.
- Keep focus indication visually distinct from elevation and hover treatment.
- Inspect clipping caused by overflow containers and stacking contexts.
- Ensure overlays preserve legibility and do not hide controls that must remain available.
- Encode shared depth in tokens or component variants, not repeated custom shadow strings.

Do not redesign the interaction pattern, modal behavior, dismissal logic, or navigation flow. Refine the representation only after those behaviors are decided.

## Stabilize images and assets

1. Render each asset at its actual delivery size and pixel density.
2. Test bright, dark, low-contrast, and visually busy images when text or controls overlap media.
3. Test the minimum and maximum supported aspect ratios for user-provided media.
4. Identify content that must not be cropped: faces, labels, product features, data, or screenshot controls.
5. Define a reusable media container, ratio policy, focal-point behavior, crop mode, and fallback where the component repeats.
6. Use a purpose-made asset or alternate crop when one source cannot serve every size credibly.

For text on media, choose a stable treatment such as a controlled overlay, protected region, solid backing surface, text shadow used for legibility, or alternate asset. Validate the final composition; an overlay is not automatically sufficient.

Keep screenshots readable at the intended size. If detail is essential, change the presentation or supply a suitable asset instead of shrinking it until it becomes texture. Inspect icons at rendered size and do not compensate for a weak source with arbitrary effects.

Do not conceal a low-quality or unsuitable source asset. State the asset limitation and the replacement or export needed.

## Refine defined states

- Inventory the states the component already supports: empty, minimal, typical, dense, loading, partial, error, success, disabled, and offline where relevant.
- Keep the primary content and action hierarchy consistent across states unless the product specification says otherwise.
- Use skeletons, spinners, placeholders, or surfaces only when the behavior has already been chosen.
- Ensure loading decoration does not imply content structure the final state cannot preserve.
- Keep errors and warnings visible without relying only on color.
- Check that empty-state illustration, spacing, and surface do not overpower the established action.
- Test abundant content, long labels, many items, missing images, and failed assets—not only the ideal populated state.
- Add state treatments to component variants and documentation when the pattern repeats.

Do not invent empty-state copy, calls to action, filters to hide, retry behavior, or state transitions. Request the missing content or interaction decision, then refine its visual representation.

## Reject misleading fixes

- Do not stack border, shadow, and surface contrast when one clear cue is enough.
- Do not increase z-index values without identifying the intended layer relationship.
- Do not place essential text over uncontrolled imagery without a robust fallback.
- Do not crop screenshots or uploads in a way that removes their task-relevant subject.
- Do not treat a decorative illustration as a substitute for missing state content or behavior.
- Do not make loading, error, and empty states visually unrelated to the component they replace.

## Verify the refinement

At a narrow and a wide viewport, inspect the changed components against adjacent surfaces and layers. Exercise the supported interactive states and use a representative media matrix.

Confirm that:

- stacking order and visual depth communicate the same relationship;
- no shadow, overlay, or border clips unexpectedly;
- focus and state cues remain distinct from decorative depth;
- text and controls remain legible over bright, dark, and busy media;
- extreme ratios and focal points do not remove essential content;
- screenshot detail and icons remain meaningful at delivery size;
- empty, loading, error, and dense states preserve hierarchy and do not shift controls unpredictably;
- shared tokens or variants replace repeated local effects.

Record the states, media cases, themes, and viewports actually rendered. Separate verified results from source-asset limitations and checks that remain pending.
