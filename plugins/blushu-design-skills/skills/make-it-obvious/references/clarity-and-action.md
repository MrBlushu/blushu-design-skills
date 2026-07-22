# Clarity and action

Use this reference to review one or more screens for first-glance comprehension, scanning, visual hierarchy, labels, and actionable controls. Do not use it as a visual-style critique.

## First-glance pass

Inspect the whole screen before reading details. Record whether the artifact answers these questions without relying on prior context:

- What is this product, page, or state?
- What can the person do here?
- What matters most for the stated task?
- Where should the person begin or continue?
- Which elements are controls, links, status, content, or promotion?

Treat unanswered questions as findings only when they divert attention from the task. Intrinsic domain reasoning is not a usability defect; avoidable interface interpretation is.

## Reconstruct the perceived hierarchy

List elements in the order they attract attention, then compare that order with task importance. Check these relationships:

| Signal | Failure | Action |
| --- | --- | --- |
| Prominence | Secondary content dominates the task entry point | Reduce competing emphasis or strengthen the required element |
| Similarity | Unrelated elements look equivalent | Differentiate role through type, treatment, or placement |
| Grouping | Related controls or content appear disconnected | Bring them into one bounded or consistently spaced region |
| Nesting | Parent-child structure is visually misleading | Align headings and containers with the actual structure |
| Sequence | Visual order conflicts with task order | Reorder or add an explicit continuation cue |

Test the hierarchy by shrinking, blurring, or viewing the screen briefly. The intended regions and primary path should remain legible without reading every word.

## Review for scanning

Assume the person searches for task-relevant words and signals instead of reading linearly.

- Make headings describe the content or decision beneath them.
- Keep a heading closer to the section it introduces than the preceding section.
- Break walls of text where a task-relevant boundary exists.
- Use lists for parallel choices or facts, not merely to decorate prose.
- Emphasize only terms that help locate or distinguish an action; excess emphasis becomes noise.
- Preserve long-form content when reading is the task. Improve its entry points and structure instead of deleting necessary detail.

Do not recommend “more whitespace” or “shorter copy” without identifying what becomes easier to find, understand, or do.

## Review labels and choices

For every task-relevant label, compare the words shown with the concept the person is likely seeking.

- Prefer familiar task language over internal, clever, promotional, or technical naming.
- Make sibling choices distinguishable without requiring the person to infer the organization's taxonomy.
- Make a destination title preserve the promise of the selected label.
- Expose secondary detail after an understandable first decision when presenting it early makes the choice harder.
- When a choice is inherently difficult, add only the minimum guidance needed at the point of decision.

Do not demand exact wording matches when the terms are obviously equivalent in context.

## Review action clarity

Identify every element required to start, continue, submit, cancel, or recover. Verify that role and state can be perceived before interaction.

- Combine position, shape, wording, contrast, and state when one cue is too weak.
- Do not rely on hover to reveal that a control exists or what it does.
- Do not style non-interactive text like a control or make controls indistinguishable from content.
- Make disabled, selected, loading, and completed states distinct without hiding the next available action.
- Preserve platform conventions unless the replacement is immediately understandable or supplies enough value to justify learning.

Subtlety is not a goal when it makes a necessary signal easy to miss. Loudness is not a goal either; make the signal strong enough for the task and context.

## Reduce noise without flattening meaning

Classify each competing element as task support, necessary context, secondary option, promotion, or decoration. Remove, defer, or quiet elements that do not contribute to the current decision. Preserve dense information when users need comparison, monitoring, or expert overview and the hierarchy remains parseable.

Prefer subtracting an obstruction before adding instructions. Add explanatory text only when layout, naming, convention, or sequence cannot make the interaction self-explanatory.

## Produce a finding

Tie each issue to all four parts:

1. **Signal:** the visible element or relationship.
2. **Interpretation cost:** the unnecessary question it creates.
3. **Task consequence:** hesitation, wrong choice, missed content, or failure to act.
4. **Verification:** brief exposure, findability check, first-click task, or task walkthrough.

If the artifact alone cannot establish the consequence, label it inferred and route the hypothesis to observational verification.
