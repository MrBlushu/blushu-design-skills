# Implementation and quality gates

## Choose the implementation path

### Existing project

1. Read package, build, lint, test, routing, component, and styling conventions.
2. Preserve the stack and design system unless a demonstrated blocker requires change.
3. Reuse accessible components and tokens before adding variants.
4. Keep edits inside the authorized project scope and preserve unrelated user changes.
5. Run the project’s existing checks in proportion to the change.

### New project

1. Choose the simplest stack that satisfies the agreed deliverable and environment.
2. Avoid dependencies that do not reduce material implementation or maintenance risk.
3. Do not bundle rigid visual templates that make unrelated sites converge.
4. Establish only the routes, components, tokens, and tooling required by the sitemap and QA gate.

## Implement the complete surface

Cover the agreed pages or sections, navigation, content hierarchy, assets, responsive behavior, CTA destinations, and applicable empty/loading/error/success/recovery states. Keep semantic structure and DOM/focus order stable across layout modes.

For forms:

- use correct labels, validation, error association, success/failure feedback, and keyboard behavior;
- connect a real endpoint only when destination, data handling, consent, and authorization are defined;
- otherwise provide a visibly non-submitting prototype or explicit integration placeholder.
- render user-controlled and persisted values with text nodes or equivalent escaping; never interpolate them into `innerHTML` or another executable markup sink.

Do not hide missing factual content inside polished UI. Keep placeholders searchable and listed in `content-gaps.md`.

Before and after implementation, compare visible copy against approved sources. Remove or label any unsourced process, material, place, response expectation, service detail, superlative, guarantee, or commercial promise. Connective copy may improve flow but must not create a new fact. Filenames, domains, colors, and image subjects are not factual sources.

## Render before claiming success

A successful build is not rendered proof. Exercise the actual site in a browser or equivalent renderer. During implementation, use one representative compact, regular, and wide width chosen from the project’s real breakpoints. Expand coverage for fragile components, supported extremes, or observed failures.

Verify one representative page per shared template, then sample sibling pages for content-specific overflow or state differences.

## Quality gate

Mark each item `pass`, `fail`, `not verified`, or `not applicable`:

- goal, architecture, deliverable, and sitemap coverage;
- factual content provenance and explicit placeholders;
- routes, navigation, anchors, CTA, links, and not-found behavior;
- form behavior and integration boundaries;
- responsive structure, supported extremes, zoom risk, and document overflow;
- keyboard flow, visible focus, landmarks, headings, labels, alt intent, and basic contrast;
- critical default, empty, loading, error, success, validation, and recovery states;
- HTML-like and script-like input through every reflected, review, confirmation, or persisted user-data path;
- runtime console errors, build, lint, typecheck, and relevant tests;
- asset loading, aspect ratio, cropping, responsive sources, and missing files;
- representative performance risks such as oversized media, layout shift, and blocking resources;
- visible high-priority text wrapping after fonts and layout stabilize;
- differences between prototype, local production build, and deployed environment.

For every `pass`, name the command, assertion, screenshot, walkthrough, or measurement that supports it. If the evidence was not executed or observed, mark `not verified`. Do not present this gate as accessibility certification, security audit, usability research, SEO guarantee, or production performance measurement.

## Correct efficiently

After a failure, fix the smallest causal scope and rerun the failed check first. Repeat the full matrix when a shared component, template, breakpoint, token, routing rule, or state model changes. Avoid duplicate screenshots when DOM, content, dimensions, and rendering are unchanged.

## Completion and degradation

Declare the agreed deliverable complete only when critical checks pass and every limitation is explicit. If rendering, an endpoint, credentials, or an external service is unavailable, deliver a safe local fallback only when it remains useful and accurately labeled. Missing rendered verification blocks a `production-ready` claim when visual behavior is critical.

Treat publishing, DNS, purchases, analytics activation, and external writes as separate authorized actions. A complete local site does not imply permission to deploy it.
