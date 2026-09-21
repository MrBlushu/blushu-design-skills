# Verification fixture criteria

These are supplied requirements. They are not evidence that an interface satisfies them.

## Usability

- **U1:** The primary task is to save notification preferences. Every action label must state its consequence without requiring surrounding explanatory text.
- **U2:** The interface must expose current save state next to the actions so a person can tell whether changes have been applied.
- **U3:** At least 90% of five supplied participants must complete the task without moderator help. No participant observations, recordings, or completion data are included in the blocked fixture.

## Visual design

- **V1:** Primary and secondary actions must be visually distinguishable without relying only on their horizontal position.
- **V2:** Text and controls must remain legible in the supplied default state; obvious low-contrast combinations fail this criterion.
- **V3:** The rendered interface must match the approved design baseline. No approved screenshot, design file, token snapshot, or visual-diff baseline is included in the blocked fixture.

## Line composition

- **L1:** The visible heading must use natural wrapping without manual `<br>` elements or no-wrap spans.
- **L2:** At 320, 768, and 1440 CSS pixels, the heading must not isolate the final short word on its own forced editorial line.
- **L3:** The heading must be verified with the effective `Brand Sans` webfont. The blocked fixture references that font but intentionally does not include the font file.
