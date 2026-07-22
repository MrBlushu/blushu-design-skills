# Blushu Design Skills

A playful, modular design workflow for building thoughtful websites with Codex and Claude Code.

Blushu Design Skills can turn a small brief, an asset folder, or an existing frontend into a structured website workflow. The bundle includes six focused design specialists and one end-to-end orchestrator.

> [!NOTE]
> Codex and Claude Code marketplace validation and clean local installation passed before publication. Model-backed Claude workflow checks were deferred because of token budget and remain recommended for a future release check.

## Complete Flow or Focused Specialist

Use `lets-build-a-site` when the deliverable is a complete website or a substantial end-to-end redesign. It inspects the available material, classifies what is missing, chooses the architecture and implementation path, calls only the specialists that are needed, and verifies the rendered result.

Use a specialist directly when the project already exists and the problem is narrower:

| Skill | Use it for |
| --- | --- |
| `before-we-make-a-mess` | Product direction, audience, outcomes, evidence, assumptions, risks, and decision gates |
| `make-it-flow` | Navigation, screen structure, workflows, controls, feedback, state, and recovery |
| `set-the-grid` | Responsive containers, columns, gutters, spans, alignment, media, and spatial rhythm |
| `check-the-style` | Visual hierarchy, typography, color, spacing, imagery, depth, and UI consistency |
| `make-it-obvious` | Comprehension, orientation, action clarity, avoidable friction, errors, and recovery |
| `break-it-right` | Semantic line breaks, punctuation boundaries, orphan words, balance, and overflow |
| `lets-build-a-site` | Asset intake, site architecture, implementation, specialist routing, and final QA |

The typical full sequence is:

```text
before-we-make-a-mess
→ make-it-flow
→ set-the-grid
→ check-the-style
→ make-it-obvious
→ break-it-right
```

This is not a mandatory checklist. A visual refinement should not repeat product discovery when the product direction is already accepted. A usability review should not redesign the grid unless the evidence points to a structural cause. Loading fewer specialists keeps the context focused, avoids contradictory decisions, and makes each handoff easier to inspect.

## Installation

### Codex

Verified with Codex CLI `0.145.0-alpha.18` from an isolated local marketplace; the GitHub source form is supported by the same CLI help:

```bash
codex plugin marketplace add MrBlushu/blushu-design-skills --ref main
codex plugin add blushu-design-skills@blushu-design-skills
```

The clean-install check discovered all seven skills. Start a new Codex session after installing the plugin, then invoke a skill explicitly by typing `$` and selecting its name, or include it directly in the prompt—for example, `$lets-build-a-site`. Version `0.145.0-alpha.18` is the tested version, not a declared minimum.

### Claude Code

Validated and installed from an isolated local marketplace with Claude Code `2.1.117`; the GitHub source form follows the same documented command syntax:

```bash
claude plugin marketplace add MrBlushu/blushu-design-skills
claude plugin install blushu-design-skills@blushu-design-skills
```

After installation, run `/reload-plugins` if the current session does not show the new skills. Claude Code namespaces plugin skills as `/plugin-name:skill-name`, for example `/blushu-design-skills:lets-build-a-site`. Version `2.1.117` is the tested version, not a declared minimum. Seven model-backed invocations remain a release gate.

## Build a Complete Website

Put the material you already have inside the project. An asset folder may contain:

- logos and brand marks;
- photographs, illustrations, icons, and video;
- approved copy and business information;
- brand or product documents;
- reference pages;
- an existing HTML, React, Next.js, or other frontend project.

Then make a compact request:

```text
Use lets-build-a-site to build a website from the material in ./assets.
Inspect the files before asking questions.
Recommend single-page or multi-page architecture from the content and goals.
Do not invent claims, prices, reviews, certifications, contacts, or business history.
```

The orchestrator should:

1. inventory the available material;
2. separate the site goal, architecture, and deliverable;
3. classify missing information as blocking, important, or optional;
4. ask only questions that materially change the result;
5. select and brief the necessary specialists;
6. implement in the existing or appropriate stack;
7. verify representative viewports, states, interactions, assets, usability, and text composition;
8. report placeholders, assumptions, unresolved decisions, and verification evidence.

See [Complete Website Requests](examples/full-website.md) for progressively constrained prompts.

## Use Specialists on an Existing Project

### Clarify Product Direction

```text
Use before-we-make-a-mess to review this feature brief.
Separate evidence, assumptions, unknowns, risks, and the decision that must be made.
Do not redesign the interface yet.
```

### Improve Navigation and Interaction

```text
Use make-it-flow on the current project.
Review the main user paths, navigation, controls, feedback, and state continuity.
Implement only changes supported by the accepted requirements.
```

### Rework the Responsive Grid

```text
Use set-the-grid to review the current layout system.
Define containers, tracks, gutters, spans, ownership, and responsive transformations.
Verify representative pages and viewport sizes.
```

### Improve the Visual Design

```text
Use check-the-style on the rendered interface.
Improve hierarchy, spacing, typography, color, imagery, depth, and component consistency.
Preserve accepted product, interaction, and structural decisions.
```

### Run a Usability Review

```text
Use make-it-obvious on the current interface and its primary user task.
Prioritize comprehension, orientation, action clarity, friction, errors, and recovery.
Separate observed evidence, visible signals, and inferred consequences.
```

### Fix Text Composition

```text
Use break-it-right on the approved visible copy.
Test the real font and representative viewport widths.
Compare natural wrapping with punctuation-aware alternatives before changing line breaks.
```

See [Existing Project Requests](examples/existing-project.md) for one reusable example per specialist.

## Missing Information and Non-Invention

The workflow classifies gaps by impact:

- **blocking:** implementation cannot continue correctly without the answer;
- **important:** the answer improves the result, but an explicit placeholder can keep work moving safely;
- **optional:** the workflow may propose an option or defer the decision.

The skills must not invent identity, testimonials, statistics, certifications, awards, prices, contact details, business history, legal promises, product capabilities, or rights to use an asset. Synthetic placeholders must be visible, searchable, and reported at handoff.

## Working Artifacts

During a complete workflow, `lets-build-a-site` may create a compact project-local record:

```text
.site-work/
├── site-brief.md
├── asset-manifest.md
├── content-gaps.md
├── site-map.md
├── design-decisions.md
├── ux-product-handoff.md
└── qa-report.md
```

The exact files depend on the work. They keep decisions inspectable without loading every prior discussion into every specialist. They belong to the website project being built, not to this plugin repository.

## Repository Structure

```text
blushu-design-skills/
├── README.md
├── .gitignore
├── .agents/
│   └── plugins/
│       └── marketplace.json
├── .claude-plugin/
│   └── marketplace.json
├── plugins/
│   └── blushu-design-skills/
│       ├── .codex-plugin/
│       │   └── plugin.json
│       ├── .claude-plugin/
│       │   └── plugin.json
│       └── skills/
│           ├── before-we-make-a-mess/
│           ├── make-it-flow/
│           ├── set-the-grid/
│           ├── check-the-style/
│           ├── make-it-obvious/
│           ├── break-it-right/
│           └── lets-build-a-site/
└── examples/
    ├── full-website.md
    └── existing-project.md
```

Codex and Claude Code use separate platform manifests and marketplaces, but both load the same portable skill files.

## Compatibility and Limits

- The core instructions use portable `SKILL.md` files and progressively loaded references.
- Platform-specific UI metadata may be ignored by a host that does not support it.
- The asset inventory helper requires Python 3 and uses only the standard library.
- Rendered QA depends on the browser, device, or preview tools available in the host environment.
- The workflow does not publish websites, change DNS, purchase services, activate analytics, or send real form submissions without explicit authorization.
- Codex local marketplace installation is verified on `0.145.0-alpha.18`; no minimum Codex version is declared.
- Claude Code marketplace validation and local installation are verified on `2.1.117`; no minimum Claude Code version is declared.
- Remote GitHub installation is checked again from a clean clone during publication.

## Principles

- Inspect existing material before asking questions.
- Keep specialist responsibilities separate.
- Load only the context needed for the current decision.
- Prefer observable evidence over taste-based claims.
- Preserve accepted decisions and project conventions.
- Do not invent missing business information.
- Verify the rendered result, not only the source code.

## License

Released under the [MIT License](LICENSE).
