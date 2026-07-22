# Intake and project classification

## Inspect before asking

1. Resolve the requested project or asset directory and stay inside its authorized scope.
2. Inspect repository state, framework, package files, build commands, pages, components, tests, and existing design tokens.
3. List documents and media by path, type, size, and metadata before reading their full contents.
4. Search documents selectively for identity, offer, audience, calls to action, proof, contacts, constraints, and canonical references.
5. Record observations separately from inferences, assumptions, unknowns, and user decisions.
6. Ask nothing that can be answered from available files.

Do not mutate project files during intake. Create `.site-work` artifacts only after the working directory and requested deliverable are resolved.

## Classify three independent axes

Always state all three axes. Do not let a value on one axis silently determine another.

| Axis | Initial values | Decide from |
| --- | --- | --- |
| Goal | showcase; landing/conversion; portfolio/catalog; editorial; service/product | primary outcome, audience, task, offer, and CTA |
| Architecture | single-page; multi-page | content volume, distinct intents, SEO needs, services, locations, audiences, and navigation paths |
| Deliverable | HTML prototype; production-ready site; change to an existing project | requested fidelity, stack, integrations, verification, and release expectations |

Attach a confidence level and supporting evidence to each decision. Treat “showcase site” as a goal, never as an automatic single-page choice.

## Classify missing information

- **Blocking:** correctness or safe implementation is impossible without it. Stop before the affected irreversible or misleading work.
- **Important:** quality changes materially, but an explicit placeholder or reversible assumption permits progress.
- **Optional:** propose a reasonable choice without fabricating facts.

Typical blocking gaps include conflicting canonical identities, an indeterminate technical deliverable, an undefined real form destination, or explicitly disputed rights to an essential asset. Missing testimonials, final photography, or social URLs are normally important rather than blocking when placeholders are safe.

### Require a minimum real brief

Before implementation, establish from user input or verified files:

- the real identity or subject of the site;
- the site purpose and intended audience or primary task;
- the requested deliverable and editable scope.

Treat any missing item above as blocking. Do not invent a brand, offer, audience, services, projects, or CTA and then label the whole site as placeholder. Placeholders may fill secondary content slots only after the minimum brief is real. A generic speculative concept is allowed only when the user explicitly asks for a concept, mockup, or placeholder prototype.

## Ask in bounded rounds

- Ask at most three short questions per round.
- Ask only about blocking gaps or important gaps with high impact.
- Explain which artifact was inspected and how the answer changes the result.
- Prefer one decisive question over several preference questions.
- Do not repeat answered questions or ask for optional taste before establishing the site goal.
- Continue without a question when explicit assumptions and placeholders preserve correctness.
- For an empty or nearly empty directory and a vague request, prioritize three questions: who or what the site represents; what outcome and audience/task it serves; what deliverable and constraints are required.

## Intake gate

Proceed to architecture and implementation only when:

- the project directory and editable scope are known;
- goal, architecture, and deliverable have a supported decision or an explicit reversible hypothesis;
- no unresolved blocking gap affects the next action;
- factual content has a traceable source or is labeled as placeholder;
- external actions such as publishing, data submission, DNS, or purchases are outside scope unless explicitly authorized.

If the gate fails, update `content-gaps.md`, ask the smallest useful question set, and stop at the decision boundary.
