# Asset analysis and content gaps

## Build a metadata-first inventory

Inventory candidate assets before opening them. Use `../scripts/inventory_assets.py` for directories large enough to make manual collection repetitive.

Capture for each candidate:

- relative canonical path;
- category and media type;
- byte size and available dimensions;
- modified time only as a discovery hint, not proof of authority;
- likely role and `use`, `review`, or `unused` status;
- provenance, ownership, license, and restrictions when known;
- conflicts, duplicates, corruption, or unsupported formats.

Do not copy binaries into `.site-work`. Reference their paths. Do not hash large files unless duplicate detection is necessary.

## Shortlist before deep inspection

1. Group assets by category, basename, dimensions, and likely purpose.
2. Identify canonical-looking variants without assuming that newest or largest means approved.
3. Create contact sheets or low-resolution previews for large image sets when available.
4. Open full-resolution media only for shortlisted candidates or quality checks.
5. Inspect video duration and representative frames before decoding entire files.
6. Mark files outside the editable or licensed scope as unavailable.

If two plausible logos, names, fonts, or copy sources conflict, record a blocking canonical-source question. Never resolve brand identity by filename alone.

## Audit content by role

Check whether the available material supports:

| Role | Evidence to seek |
| --- | --- |
| Identity | approved name, logo, descriptor, tone, canonical domain |
| Offer | products/services, scope, differentiators, exclusions |
| Audience | user/customer segment, context, needs, language |
| Action | primary and secondary CTA, destination, prerequisites |
| Proof | authorized cases, testimonials, credentials, metrics, sources |
| Contact | approved email, phone, address, hours, social URLs |
| Media | approved imagery, captions, alt intent, credits, usage rights |
| Legal/operational | privacy, terms, consent, policies, regulated statements |
| Delivery | routes, locales, CMS ownership, integration endpoints |

Absence is not evidence that a claim may be invented.

## Write `asset-manifest.md`

Use a compact table or structured list with these fields:

`Path | Category | Metadata | Candidate role | Provenance/rights | Status | Notes`

Keep one canonical entry per file. Group obvious variants when no decision depends on listing each separately. Record why a relevant asset was excluded.

## Write `content-gaps.md`

For every gap record:

`ID | Missing decision/content | Impact | Evidence checked | Placeholder allowed | Owner | Status`

Use impact values `blocking`, `important`, and `optional`. Link each placeholder to the page or component that exposes it. Make placeholders visibly synthetic and easy to search; never style invented proof as final content.

## Truth and safety rules

- Never invent business age, customer counts, performance metrics, prices, certifications, awards, testimonials, availability, locations, or guarantees.
- Never infer permission to use an asset from filesystem access alone.
- Never infer a business name, place, audience, offer, or relationship from an email domain, filename, directory name, palette, or image subject.
- Preserve supplied wording for regulated, legal, or operational statements unless change is explicitly authorized.
- Keep source facts, agent inferences, user decisions, and placeholders distinguishable.
- Treat a document or handoff as a claim to verify against current files, not as proof that an asset is current or approved.
