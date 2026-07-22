# Data and input

Use this reference to design data exploration, immediate filtering, value entry, defaults, validation, and recoverable error handling.

## Contents

- [Model the data task](#model-the-data-task)
- [Exploration patterns](#exploration-patterns)
- [Entry patterns](#entry-patterns)
- [Validation and errors](#validation-and-errors)
- [Composition checks](#composition-checks)

## Model the data task

Identify whether the user is trying to:

- locate a known item;
- narrow an unknown set;
- compare values or distributions;
- identify an outlier or relationship;
- enter a known value;
- translate an imprecise value into a structured one;
- correct invalid or conflicting data.

Declare data volume, update frequency, latency, missing values, permissions, source of truth, and whether queries change the URL or history. Keep filter state distinct from selected-item state and draft-input state.

## Exploration patterns

### Datatips and data spotlight

- **Problem/context:** reveal precise or contextual detail for a mark, row, point, or region without permanently crowding the overview.
- **Fit:** users scan an overview and inspect a small number of targets; detail is supplemental and target identity is stable.
- **Avoid:** essential information exists only on hover, many items require simultaneous comparison, or targets are too dense to acquire reliably.
- **System effects:** keep summary content primary; bind transient detail to target state; avoid changing place; show focus, loading, missing, and selected detail clearly.
- **Variants:** hover/focus datatip, click-pinned detail, or spotlight/highlight with side detail.
- **Dependencies:** target hit testing, stable keys, focus support, and collision handling.
- **Verify:** keyboard, touch, and pointer can reveal equivalent detail, pinned state survives intended updates, labels match targets, and overlays never obscure the active value irrecoverably.

### Dynamic queries

- **Problem/context:** let users narrow or reshape a dataset and see results update as criteria change.
- **Fit:** feedback is fast enough to support exploration; filters map to understandable attributes; users benefit from seeing the remaining set.
- **Avoid:** each query is costly or destructive, results update too slowly without explicit submission, or filter interaction creates unstable layout and lost selection.
- **System effects:** keep filters and result count visible; store query separately from committed selection; update results in place; show applying, empty, partial, stale, failed, and reset states.
- **Variants:** immediate controls, debounced text, faceted filters, or explicit Apply for expensive batches.
- **Dependencies:** cancellable queries, URL/state serialization, caching, and stale-response control.
- **Verify:** every filter visibly affects results, rapid changes cannot show out-of-order data, zero results remain recoverable, Back/share restoration follows policy, and reset is predictable.

### Overview plus contextual detail

- **Problem/context:** preserve the shape of a dataset while explaining a selected subset or item.
- **Fit:** users alternate between pattern recognition and precise inspection; selection should remain visible in context.
- **Avoid:** detail dominates the task, multiple items need dense attribute comparison, or overview and detail use incompatible data scopes.
- **System effects:** coordinate summary and detail content; share selection identity; keep navigation local or deep-linkable; expose selected, loading, stale, and unavailable detail.
- **Variants:** linked chart/table, spotlight, split detail, or drilldown on narrow screens.
- **Dependencies:** synchronized selection, scale/domain policy, and responsive transformation.
- **Verify:** selected detail and overview highlight always agree, filters affect both consistently, missing items recover safely, and narrow layouts preserve return context.

## Entry patterns

### Forgiving and structured input

- **Problem/context:** accept values in the form users know while producing reliable structured data.
- **Fit:** several common formats are unambiguous or can be normalized with confirmation; rigid formatting would cause avoidable errors.
- **Avoid:** ambiguity has safety or financial consequences, silent normalization changes meaning, or parsing quality is insufficient.
- **System effects:** show examples near the field; retain raw and parsed state when needed; keep form navigation stable; explain recognized, ambiguous, corrected, and rejected values.
- **Variants:** tolerant parser, masked/segmented field, structured controls, or confirmation of interpretation.
- **Dependencies:** locale rules, parser tests, and canonical storage.
- **Verify:** representative valid formats parse identically, ambiguous input requests clarification, pasted values work, correction preserves user intent, and stored/displayed values round-trip.

### Autocomplete

- **Problem/context:** reduce typing and help select a valid or known value from a large set.
- **Fit:** users know part of the value; suggestions can arrive promptly; choosing an entity is safer than free text.
- **Avoid:** tiny option sets, suggestions are unreliable or privacy-sensitive, or free-form values are valid but the UI implies they are forbidden.
- **System effects:** keep typed text and selected entity distinct; store query/highlight/selection; avoid leaving the form place; show loading, no match, error, and accepted free text.
- **Variants:** local suggestions, remote search, tokenized multi-select, or creatable value.
- **Dependencies:** debouncing, cancellation, stable identifiers, ranking, and keyboard model.
- **Verify:** typing, arrows, enter, escape, blur, touch, and paste behave coherently; late results cannot replace newer ones; chosen label and stored identity remain aligned.

### Good defaults

- **Problem/context:** prefill a likely safe value to reduce repetitive work and communicate normal configuration.
- **Fit:** evidence supports a common choice; the value is reversible and visible; personalization is reliable.
- **Avoid:** default consent, destructive scope, biased choice, stale personal data, or a value users may submit without noticing.
- **System effects:** distinguish default from user-entered content; track whether it was accepted or changed; do not change navigation; explain derived, unavailable, or reset values.
- **Variants:** system default, previous choice, contextual suggestion, or recommended value.
- **Dependencies:** provenance, freshness, permissions, and reset behavior.
- **Verify:** default is valid for the current context, visible before submission, easy to replace, not silently restored over edits, and analytics do not confuse acceptance with intent.

## Validation and errors

### Inline validation

- **Problem/context:** identify correctable field-level problems close to the input before or during submission.
- **Fit:** rules are local and certain; early feedback prevents wasted work; correction does not require server authority.
- **Avoid:** scolding while the user is still composing, duplicating server rules inaccurately, or marking an untouched optional field invalid.
- **System effects:** reserve space for guidance; track touched/dirty/valid state; keep focus progression under user control; show pending, valid, warning, and error without color alone.
- **Variants:** on blur, after pause, or on submit then live correction.
- **Dependencies:** shared validation rules, accessible descriptions, and stable error placement.
- **Verify:** feedback timing does not interrupt entry, message names the fix, invalid values remain editable, corrected state clears accurately, and screen readers receive the association.

### Error messages and recovery

- **Problem/context:** explain why an input or submission failed and provide a specific path to recovery.
- **Fit:** any validation, permission, conflict, connectivity, or server failure can block progress.
- **Avoid:** generic banners detached from fields, clearing user input, exposing internal errors, or suggesting retry for permanent failures.
- **System effects:** preserve affected content and drafts; attach field and form errors to authoritative state; navigate/focus to the first actionable issue without trapping users; distinguish retry, edit, sign-in, conflict resolution, and support paths.
- **Variants:** inline field error, form summary, conflict panel, or persistent status.
- **Dependencies:** error taxonomy, safe message mapping, focus management, and telemetry correlation.
- **Verify:** each failure class yields the right action, submitted values remain available, summaries link to fields, repeated submission is safe, and recovery removes stale errors.

### Review before consequential submission

- **Problem/context:** let users confirm a structured set of high-impact values before an irreversible or externally visible action.
- **Fit:** consequences are material; data spans several sections; errors are easier to spot in a summary.
- **Avoid:** routine reversible submissions, a review that merely repeats unreadable form controls, or a false promise of reversibility.
- **System effects:** summarize committed candidate data; keep draft source intact; add edit-return navigation; show changed, missing, warning, submitting, and completed states.
- **Variants:** confirmation summary, diff preview, or final wizard step.
- **Dependencies:** stable draft, section links, validation snapshot, and idempotent commit.
- **Verify:** summary uses meaningful labels and units, edit returns preserve position/data, last-minute changes invalidate stale review, and commit outcome is explicit.

## Composition checks

- Keep query, selection, draft, validation, and committed data as distinct state domains.
- Cancel obsolete remote requests and ignore late responses by request identity.
- Preserve filters and draft input across detail inspection according to declared lifetime.
- Show active criteria and provide a reachable reset or clear action.
- Never rely on placeholder text as the only label or format instruction.
- Make error recovery local when possible and provide a summary when errors span hidden regions or steps.
- Test empty, partial, malformed, permission-limited, offline, conflicted, and very large data states.
- Verify normalization, dates, numbers, units, and sorting with the actual supported locales instead of assuming one format.
