# Choosing single-page or multi-page architecture

## Keep the decision independent

Decide architecture after classifying the site goal and before visual refinement. A showcase, portfolio, or landing goal may use either architecture. The deliverable type also remains independent.

## Favor single-page when

- one audience follows one dominant narrative or CTA;
- content is concise enough to scan without hiding distinct tasks;
- sections do not need independent search intent, ownership, or sharing;
- navigation can remain a small set of anchors;
- maintenance benefits from one coherent content surface;
- the site does not require many detail records or durable sub-routes.

Do not choose single-page merely because implementation is faster.

## Favor multi-page when

- users arrive with several distinct intents or audiences;
- services, products, projects, articles, locations, or policies need durable URLs;
- content volume would make one page long, repetitive, or hard to orient within;
- search discovery depends on differentiated topics and metadata;
- multiple templates or detail records have stable information architecture;
- governance, localization, analytics, or editing ownership differs by section;
- navigation must support comparison, return visits, or deep linking.

Do not claim SEO improvement as guaranteed. State which discoverability or indexing need the route structure supports.

## Decide with content, not labels

1. List primary audiences, intents, tasks, and CTA destinations.
2. Group content by distinct user question, not by available filenames.
3. Identify content needing its own URL, metadata, lifecycle, or template.
4. Estimate whether the main path stays coherent without excessive anchors or repeated context.
5. Test both candidate structures against navigation, sharing, maintenance, and future content.
6. Select the simpler architecture that satisfies known needs and record conditions that would trigger migration.

When evidence is incomplete but not blocking, choose a reversible architecture and label the assumption.

## Draft `site-map.md`

For single-page sites, record:

`Section | User question | Content/source | CTA | Anchor | Dependencies`

For multi-page sites, record:

`Route | Page/template | User intent | Content/source | Primary CTA | Parent/related routes`

Also record global navigation, footer/legal destinations, error/not-found behavior when applicable, and which pages share a template.

## Architecture decision record

Add to `design-decisions.md`:

- selected architecture and confidence;
- goal and deliverable it serves without conflating them;
- evidence and constraints;
- strongest rejected alternative;
- tradeoffs accepted;
- conditions that require revisiting the choice.

Reopen architecture only for new content families, distinct user intents, governance constraints, or observed navigation failure. Do not reopen it for visual preference.
