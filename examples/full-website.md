# Complete Website Requests

These prompts use `lets-build-a-site` with progressively richer input. Replace generic paths and constraints with the real project material. Do not include claims or business facts that have not been approved.

## 1. Minimal Input

```text
Use lets-build-a-site to create a small website for this project.
Inspect the current directory before asking questions.
Identify the site goal, recommend single-page or multi-page architecture, and choose an appropriate implementation.
Ask only for information that blocks a correct result.
Use explicit placeholders for important missing content and report every placeholder at handoff.
Do not invent identity, claims, prices, testimonials, certifications, contacts, or business history.
```

## 2. Input with Assets

```text
Use lets-build-a-site to build a complete website using the approved material in ./assets and the existing copy in ./content.
Inventory logos, images, video, documents, and copy before proposing the architecture.
Explain which assets are usable, which need clarification, and which content gaps are blocking, important, or optional.
Select only the design specialists needed for this project.
Implement the site, preserve original asset files, and verify the rendered result across representative viewport sizes.
Do not infer rights, claims, prices, reviews, certifications, or contact details from filenames or visual appearance.
```

## 3. Input with Constraints

```text
Use lets-build-a-site to build a production-ready informational website from ./assets and ./content.

Constraints:
- keep the existing framework and package manager;
- support 360 px, 768 px, 1024 px, and 1440 px viewports;
- preserve the approved logo and written copy;
- use no external fonts or stock imagery;
- keep motion optional and respect reduced-motion preferences;
- do not add analytics, cookies, external form delivery, deployment, or DNS changes;
- meet the existing accessibility requirements without claiming certification;
- separate observed QA evidence from assumptions.

Inspect the project first. Recommend the architecture from the content and user goals, call only the specialists that resolve real gaps, implement the site, and produce a final report covering placeholders, tested states, viewport evidence, and remaining decisions.
```
