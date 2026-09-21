---
name: lets-build-a-site
description: Build or complete end-to-end websites from sparse briefs, documents, copy, images, video, asset folders, or existing code by inspecting materials first, choosing the site goal, single-page or multi-page architecture, and deliverable, coordinating only needed UX/UI specialists, implementing in the appropriate stack, and verifying the rendered result. Use for complete landing pages, showcase sites, portfolios, catalogs, editorial sites, product or service websites, full redesigns, and completion of existing web projects. Do not use for isolated discovery, interaction, grid, visual, usability, line-composition, copywriting, debugging, audits, or deployment-only requests without an end-to-end website deliverable.
---

# Let's Build a Site

## Resolve the execution profile

Resolve this before the mandatory intake reference, project inspection, or creation of working artifacts:

- **create:** produce a new site architecture, plan, implementation, or complete site; write only when the task authorizes creation;
- **change:** modify an existing site within the named scope, but write only with separate task-supplied authorization;
- **review:** inspect a supplied site or plan for open end-to-end problems without modifying files;
- **verify:** test only declared website acceptance criteria or final-QA claims on completed work; always remain read-only.

Choose the profile from an explicit token after the skill name, then an explicit handoff `Mode`, then unambiguous request language, otherwise preserve the existing end-to-end build behavior when the request actually supplies a concrete site task. A profile never grants write authority.

After resolving any profile, require a concrete site task or question, usable scope or artifact, and any authority the profile needs. If the request or workflow handoff supplies only the skill name, profile token, or `Mode` without that task context, and no usable recent context resolves it, return only the resolved `Mode` or `Mode: unresolved`, `Status: NEEDS_TASK`, the missing task fields, and `Mutations: none`; then stop before project inspection, reference loading, routing, or working-file creation.

For a workflow `verify` handoff, require `Question`, `Scope`, `Baseline`, `Criteria`, `Authority: read-only`, `Locked Decisions`, `Invocation ID`, `Artifact Revision`, and `Pass Limit: 1`. Recover a direct conversational task from the immediately preceding context only when artifact, closed question, scope, baseline, and criteria have one strongly supported interpretation. Otherwise return only `Mode: verify`, `Status: NEEDS_TASK`, the missing fields, and `Mutations: none`.

In its own `verify` profile, check only declared acceptance criteria and directly affected neighboring state in one bounded pass. Load only references needed to interpret those criteria and use real build or rendered evidence when required. Retry one tool action only for a clearly transient safe failure. Do not mutate files, designs, configuration, external systems, or `.site-work`; do not rebuild, redesign, broaden into general QA, or recommend or apply a repair; do not invoke another skill, including a specialist; and do not execute a handoff or `Next Task`.

End `verify` with `Mode`, terminal `Status: PASS | FAIL | BLOCKED`, checked `Scope`, criterion-specific `Evidence`, `Failed Criteria`, optional uninvestigated `Out-of-scope Signals`, `Owner` for a failure, and `Mutations: none`. `PASS` needs evidence for every criterion; use `BLOCKED` when decisive rendering, build evidence, an artifact, or a required tool is unavailable.

This terminal report replaces normal site delivery. In `verify`, retain only evidence, selective reference, and quality-gate rules needed for the declared criteria; skip intake expansion, inventory, architecture, planning, implementation, correction, specialist routing, working artifacts, recommendations, and handoffs.

## Operating contract

Own intake, architecture integration, implementation, rendered QA, and delivery. Delegate only decisions that need a specialist. Invoke specialists one at a time; verify their artifacts before preserving their decisions.

Inspect available files before asking questions. Never invent identity, claims, prices, testimonials, certifications, metrics, contacts, rights, or promises. Treat publishing, DNS, purchases, analytics activation, real form submission, and other external writes as separate actions requiring explicit authority.

Keep the core workflow tool-agnostic so it runs in Codex and Claude Code. Use host-specific tools only as interchangeable ways to inspect, edit, render, and verify.

## Specialist verification routing guard

This section applies only when a non-verify orchestration workflow dispatches a specialist in that specialist's `verify` profile. It does not permit `lets-build-a-site` to invoke a specialist during its own `verify` profile.

Before invoking a specialist verifier, resolve one closed question, artifact scope, baseline, stable criterion IDs and observable conditions, locked decisions, sequence ID, invocation ID, verification ordinal, stable artifact revision, and `Pass Limit: 1`. Read `references/specialist-routing.md` and send the complete verification envelope; never forward only a skill name or mode token. Keep ledger state in memory for the entire `verify -> change -> verify` sequence so tracking the pass cannot mutate the artifact or repository.

A specialist `PASS`, `FAIL`, or `BLOCKED` is terminal for that verification invocation. Do not turn a failure into an automatic repair, follow a returned handoff, or invoke another specialist. A repair requires separate explicit `change` authority. After an authorized change creates a new artifact revision, allow at most one targeted reverification of the failed criterion. Never rerun the same skill and question against an unchanged revision.

While the specialist `verify` invocation is active, skip every instruction below that creates or updates `.site-work`, `qa-report.md`, design-decision records, handoffs, or other files. Keep its required records in memory and return its terminal report to the outer orchestrator. After a nested `PASS`, resume the authorized outer non-verify profile (`create`, `change`, or `review`). A nested `FAIL` or `BLOCKED` terminates only that verification step: record its result and owner in memory, do not repair automatically, and let the outer workflow report the unresolved gate without treating the specialist report as the site's final response.

## Load references progressively

- **At every non-verify start after profile preflight:** read `references/intake-and-classification.md` before questioning the user or editing the project.
- **When the request includes assets, documents, copy, media, or missing content:** read `references/assets-and-content-gaps.md`. Run `scripts/inventory_assets.py` when manual metadata collection would be repetitive.
- **When architecture is not already accepted or a sitemap must be created:** read `references/architecture-single-vs-multi.md`.
- **Before invoking a specialist, accepting its return, or reopening an upstream decision:** read `references/specialist-routing.md`.
- **Before editing code and again before final QA:** read `references/implementation-and-quality-gates.md`.
- **Before creating `.site-work`, sending a specialist handoff, or writing the final response:** read `references/handoffs-and-site-work.md`.

Do not load all references by default.

## Workflow

1. **Resolve scope.** Identify the project or asset directory, editable boundary, requested outcome, constraints, and whether the deliverable is a prototype, production-ready site, or change to existing code. Inspect repository state and current implementation without mutating it.
2. **Inventory before opening.** List asset and document metadata, then inspect only shortlisted files and relevant document sections. Record provenance, rights, conflicts, and unsupported material without copying binaries into working notes.
3. **Classify independently.** State the site goal, single-page or multi-page architecture, and deliverable as three separate decisions with evidence and confidence. Treat labels such as “showcase site” as goals, not architecture choices.
4. **Gate missing information.** Classify gaps as blocking, important, or optional. Require a real identity or subject, site purpose, intended audience or primary task, and deliverable before implementation; placeholders cannot replace this minimum brief. Ask at most three short questions per round, only after inspection and only when the answers materially change correctness. Proceed with explicit placeholders for other non-blocking gaps; stop at unresolved blocking gaps. Build a speculative generic concept only when the user explicitly requests one.
5. **Create compact truth sources.** Maintain the relevant `.site-work` artifacts. Keep facts, observations, inferences, assumptions, unknowns, placeholders, and user decisions distinct.
6. **Plan the site.** Define content roles, routes or sections, shared templates, navigation, CTA destinations, and completion criteria. Record durable decisions and their reopen conditions.
7. **Route adaptively.** Use only specialists whose trigger is present. Give each one a single owned question and a handoff of at most 400 words. Record every specialist as `used` or `skipped` with a concrete reason.
8. **Implement completely.** Preserve an existing stack and design system unless blocked. For a new project, choose the simplest stack that satisfies the deliverable. Build the agreed pages, states, responsive behavior, assets, interactions, and safe integration boundaries. Trace every visible factual claim, process, place, material, response expectation, and promise to approved content; do not infer facts from filenames, email domains, or visual tone. Render user-controlled values as text, never executable markup.
9. **Render and correct.** Exercise the real site at representative project widths and states. Route findings back to their owner, apply the smallest causal fix, and rerun the affected check before expanding regression coverage.
10. **Pass the quality gate.** Verify the build and rendered result, update `qa-report.md`, and distinguish `pass`, `fail`, `not verified`, and `not applicable`. Mark `pass` only when the report names the executed or observed evidence. Do not claim production readiness when a critical rendered check is unavailable.
11. **Deliver.** Report the site path, run and verification commands, architecture, coverage, specialist routing, approvals needed, placeholders, disconnected integrations, and concrete residual risks.

## Specialist routing

| Specialist | Use | Skip | Interrupt and hand off when |
| --- | --- | --- | --- |
| `before-we-make-a-mess` | audience, problem, outcome, offer, CTA, evidence, or risk may change what to build | the product frame is accepted and work is executable | evidence is insufficient for a product gate or sources conflict materially |
| `make-it-flow` | navigation, regions, states, transitions, input, feedback, or recovery are unresolved | standard informational behavior is sufficient or already specified | the decision belongs to product, structural geometry, or visual treatment |
| `set-the-grid` | containers, tracks, spans, alignment, rhythm, media, or responsive transformations need a coordinated system | the existing structural system covers the site | semantic behavior must change, or the issue is only local visual/text treatment |
| `check-the-style` | a concrete artifact needs hierarchy, typography, color, imagery, local spacing, depth, or state refinement | the existing visual system already produces a coherent result | the cause is product, behavior, systemic grid, usability evidence, or copy |
| `make-it-obvious` | a rendered interface and realistic task can reveal comprehension, orientation, action, or recovery cost | no interface is evaluable, or the request is only visual or textual | a causal fix requires a new pattern, systemic grid change, visual system, or copy decision |
| `break-it-right` | stable visible copy shows concrete breaks, orphans, imbalance, or overflow | copy, font, components, or layout are unstable, or no signal exists | a fix requires rewriting approved copy or changing shared type, grid, or breakpoints |

Preserve each specialist’s ownership. Reopen an accepted decision only when verified new evidence creates a blocking contradiction, and name both the evidence and the decision being reopened.

## Required state handling

| State | Response |
| --- | --- |
| Assets absent or directory empty | Stop before implementation when identity or subject, purpose, audience/task, or deliverable is unknown. Ask up to three high-value questions. Use placeholders for secondary content only after the minimum brief is real; never fabricate substitute proof or identity. |
| Documents contradictory | Record the competing paths and claims, classify the conflict as blocking when canonical truth changes, and ask the smallest resolving question. |
| Copy incomplete | Map every gap to a page or component; continue only with explicit, searchable placeholders when meaning and claims remain safe. |
| Existing project | Preserve stack, conventions, components, tokens, tests, and unrelated user changes; do not introduce a new framework for convenience. |
| Stack unspecified | Infer from existing code; for a new project choose the simplest environment-compatible option that meets the deliverable and record the choice. |
| Visual QA unavailable | Run available static and build checks, mark rendering `not verified`, and withhold a production-ready claim when visual behavior is critical. |
| Specialist unavailable or failed | Do not imitate its source-specific method. Continue with generic reasoning only for low-risk verifiable work; otherwise stop. Outside `verify`, retry once only for a clearly transient safe failure. In `verify`, the active specialist may retry one transient tool action but the orchestrator must not start another specialist pass. |
| External integration unavailable | Keep it disconnected or mocked and labeled; do not insert secrets, bypass authorization, or imply that submission works. |

## Artifacts and handoffs

Outside `verify`, maintain as needed under `.site-work/`: `site-brief.md`, `asset-manifest.md`, `content-gaps.md`, `site-map.md`, `design-decisions.md`, `ux-product-handoff.md`, and `qa-report.md`. Never create or update these artifacts during `verify`.

Use the common handoff fields `Goal`, `Evidence`, `Constraints`, `Decisions`, `Open Risks`, `Artifacts`, and one `Next Task`. Keep the handoff under 400 words and pass paths rather than copied artifacts. A handoff is context to verify, not proof.

Refresh the working handoff at closeout. Do not leave a `Next Task` that the current run already completed; use the next unresolved approval or state that orchestration is complete.

## Quality gate

Require evidence proportional to the deliverable for:

- sitemap and factual-content coverage, including explicit placeholders;
- routes, navigation, CTA, links, forms, states, and recovery;
- responsive behavior, supported extremes, and document overflow;
- keyboard flow, visible focus, semantic structure, labels, alt intent, and basic contrast;
- runtime errors, build, lint, typecheck, and relevant tests;
- safe handling of HTML-like and script-like user input wherever values are reflected, reviewed, or persisted;
- asset loading, cropping, responsive sources, and obvious performance risks;
- final high-priority text wrapping after fonts and layout stabilize.

Treat the gate as implementation QA, not accessibility certification, security audit, usability research, SEO guarantee, or production performance measurement.
