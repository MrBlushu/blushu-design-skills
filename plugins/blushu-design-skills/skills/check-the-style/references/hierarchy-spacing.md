# Hierarchy and spacing

Use this reference to diagnose and refine visual priority, grouping, density, intrinsic sizing, and the responsive proportions of existing components. Preserve the product decisions, content priority, interaction model, and overall grid already in force.

## Recover the intended hierarchy

1. Identify the task, content priority, and primary action already established by the product or design context.
2. List the visible roles: primary content, supporting content, labels, metadata, primary action, secondary action, and decoration.
3. Observe the rendered interface before editing. Record what attracts attention first, what reads as a group, and what competes unexpectedly.
4. Remove color mentally or inspect a grayscale rendering. Confirm that order and grouping still survive.
5. If the intended priority is unknown, make only a narrow, reversible assumption. Stop the portion that would require changing product or interaction decisions.

Treat unreadable content, ambiguous grouping, hidden controls, and clipped content as functional visual corrections. Treat a weak but understandable order or inconsistent rhythm as verifiable visual improvement. Treat ornamental emphasis and aesthetic personality as preference unless an approved direction makes them a requirement.

## Adjust emphasis deliberately

- Use weight, contrast, size, position, whitespace, and surface treatment as a coordinated set rather than pushing every dimension at once.
- Reduce competing emphasis before enlarging or decorating the primary element.
- Keep one dominant signal per local region unless the task truly contains multiple equal priorities.
- Make labels and metadata quieter only when they remain legible and their relationship to the value stays clear.
- Preserve the discoverability of actions. A secondary action may be quieter without becoming indistinguishable from static text.
- Check icons at their rendered size and in context. Do not let decorative icons outrank content or actions.
- Encode recurring emphasis as a semantic text role, component variant, or action hierarchy rather than a page-only override.

Do not rename labels, promote a different action, hide content, or change the interaction sequence to solve a visual hierarchy problem. Hand those decisions to the relevant product, content, or interaction owner.

## Establish grouping through spacing

1. Mark the smallest meaningful groups inside the component.
2. Compare internal gaps with the gaps between groups.
3. Make between-group distance perceptibly greater than within-group distance when no stronger separator carries that relationship.
4. Select values from the existing spacing scale whenever it can express the distinction.
5. Consolidate nearly identical recurring values only after confirming that they serve the same semantic relationship.
6. Apply the rule to the shared component or token when the pattern repeats; avoid a chain of local margin patches.

Use explicit separators when spacing alone would consume too much room or when dense data needs a stronger boundary. In high-density tools, preserve deliberate compactness while keeping groups parseable. Do not apply a universal instruction to “add more whitespace.”

## Control intrinsic size and responsive scale

- Size controls and content containers from their content and task, not solely from the available width.
- Add a maximum width when long measures or stretched controls weaken reading and scanning.
- Separate fixed, intrinsic, and flexible parts of a component instead of scaling every part by one percentage.
- Tune large properties and small properties independently across viewports. A heading, panel, icon, and gap do not need the same scale factor.
- Preserve useful density on wide screens and sufficient separation on narrow screens.
- Test minimum, typical, and maximum realistic content. Include long labels, large values, localization expansion, and wrapped metadata when supported.
- Record dimensional constraints as component behavior or variants when they recur.

Correct component proportions, width constraints, density, and local breakpoint behavior here. Route a request to define the complete column, module, gutter, and breakpoint architecture to the grid-system specialist.

## Reject misleading fixes

- Do not make every heading larger when the real problem is competing secondary contrast.
- Do not use color as the only separator between roles or groups.
- Do not alternate spacing values merely to create visual variety.
- Do not center content whose task depends on scanning aligned labels, values, or controls.
- Do not force full-width controls when their content or action is intrinsically compact.
- Do not compress mobile spacing uniformly until touch targets and grouping become ambiguous.
- Do not preserve desktop proportions when a narrow viewport changes reading order or available measure.
- Do not solve a repeated component problem with page-specific selectors.

When two visual treatments are equally clear, prefer the one already supported by the design system and requiring fewer exceptional rules.

Escalate unresolved priority conflicts instead of encoding them as visual compromise.

## Verify the refinement

Render at least one narrow and one wide representative viewport when the interface is executable.

At each viewport, check:

- the first visual target matches the established task priority;
- supporting roles remain visible without competing with the primary role;
- groups are distinguishable without relying on accidental alignment;
- primary and secondary actions remain discoverable in default, hover, and focus states when available;
- no label, value, icon, or control is clipped or forced into an implausible width;
- density changes are intentional rather than a desktop layout uniformly shrunk;
- repeated components use the same hierarchy and spacing rule;
- extreme content does not reverse the intended order or collapse the grouping.

Compare before and after using the same content and viewport. State which hierarchy or grouping signal changed and what rendered evidence confirms the improvement. If rendering is unavailable, report the intended check as pending rather than claiming success.
