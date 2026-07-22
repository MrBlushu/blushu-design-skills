# Verification

Use this reference to review an existing interface or prove that an implemented pattern supports the intended task, state model, navigation, feedback, recovery, and input modes.

## Contents

- [Set the evidence boundary](#set-the-evidence-boundary)
- [Build scenario coverage](#build-scenario-coverage)
- [Inspect state transitions](#inspect-state-transitions)
- [Check navigation and continuity](#check-navigation-and-continuity)
- [Check input and responsive behavior](#check-input-and-responsive-behavior)
- [Check latency and recovery](#check-latency-and-recovery)
- [Report findings](#report-findings)

## Set the evidence boundary

Classify claims before judging the interface:

- **Observed:** reproduced in a live interface, recording, screenshot, prototype, code path, or test.
- **Inferred:** supported by artifacts but not exercised directly.
- **Assumed:** necessary placeholder with no supporting artifact.
- **Unknown:** materially affects the decision and cannot be resolved from available evidence.

Record the artifact, viewport, input method, role, data condition, and build/version when available. Do not claim user behavior, compliance, or platform rules from static code alone.

In review mode, remain read-only. In implementation mode, verify the changed surface and relevant neighboring behavior after editing.

## Build scenario coverage

Start with the primary task, then add only alternate paths that can change safety, continuity, or pattern fit.

| Scenario | Setup | Action | Expected place | Expected state | Expected feedback |
| --- | --- | --- | --- | --- | --- |
| Direct entry | deep link/new session | open target | declared destination | valid initial state | orientation visible |
| Normal completion | valid data | primary action | result/return place | committed once | completion clear |
| Invalid attempt | invalid or missing data | continue/submit | remain actionable | draft preserved | correction specific |
| Empty data | no items/results | enter surface | stable empty place | filters/draft valid | next action clear |
| Slow operation | delayed response | start work | no accidental move | one request active | progress truthful |
| Failure | transient/permanent error | execute | recoverable place | data preserved | retry/edit path correct |
| Interruption | navigate, refresh, suspend | return | declared restored place | correct lifetime restored | stale/conflict shown |
| Permission change | revoke access | revisit/action | safe fallback | private state cleared | reason and next step |

Add pattern-specific cases from each retained pattern's verification field. A generic checklist cannot replace its concrete pass criteria.

## Inspect state transitions

Create a transition table for consequential state:

| From | Event | Guard | To | Visible change | Recovery |
| --- | --- | --- | --- | --- | --- |
| ready | start | eligible | running | progress, duplicate protection | cancel if supported |
| running | complete | current request | success | authoritative result | next action |
| running | fail | retryable | error | draft/result retained | retry |
| running | cancel | interruptible | cancelling | cancel acknowledged | return policy |

Check that:

- a single owner controls each state transition;
- the UI cannot display mutually impossible states;
- duplicate events are idempotent or blocked safely;
- late and out-of-order responses cannot overwrite current work;
- validation, permission, and connectivity failures have different recovery;
- transient visual state is not the only record of a durable outcome;
- partial success names what changed and what did not;
- loading, empty, error, and stale content cannot be confused.

Inspect code state and rendered behavior. Component names or reducer labels are not proof that users receive the intended feedback.

## Check navigation and continuity

Exercise:

- declared entry points, including direct links and restored sessions;
- forward movement, system/browser Back, in-product Back, Close, Cancel, and Done;
- refresh, deep link, duplicate tab/window, and return after interruption;
- switching view, tab, workspace, item, filter, and viewport mode;
- dismissal by button, escape, outside click, gesture, and navigation when supported;
- deleted, stale, renamed, or permission-lost destinations.

For each boundary, verify the intended lifetime of:

- selected object and multi-selection;
- scroll, cursor, zoom, and expanded regions;
- filters, sort, query, and loaded range;
- draft values, dirty status, validation, and preview;
- undo/redo history and background tasks;
- focus origin and return target.

Flag both unexpected loss and unsafe persistence. Restoring stale, private, or incompatible state can be worse than resetting it.

## Check input and responsive behavior

### Keyboard and focus

- Reach every primary and contextual action without a pointer.
- Confirm focus order follows the visible and task order.
- Enter overlays at a meaningful control and restore focus on exit.
- Verify arrow-key models only where the component semantics require them.
- Keep visible focus during loading, validation, reflow, and virtualized updates.
- Ensure shortcuts do not conflict with text entry, browser, or platform conventions.

### Touch and pointer

- Provide visible alternatives to hover, right-click, precision drag, and double-click.
- Prevent accidental activation during scrolling or selection.
- Keep menus, datatips, and drag targets reachable near viewport edges.
- Verify cancel/undo for gestures with consequential effects.

### Responsive transformation

At representative narrow, middle, and wide widths, verify:

- the same primary task can be completed safely;
- split views, grids, panels, tabs, and overlays transform deliberately;
- selected item and draft survive the transformation when intended;
- no primary action or status becomes clipped, covered, or gesture-only;
- virtual keyboard, orientation change, zoom, and long content do not hide completion or errors;
- source and visual order remain coherent.

Use current authoritative sources when exact platform or accessibility requirements matter. Do not treat remembered numeric values as certification evidence.

## Check latency and recovery

Test at least instant, perceptible, slow, failed, and recovered responses when the interface depends on remote work.

Verify:

1. feedback starts soon enough to connect it to the action;
2. progress type matches what the system can measure;
3. useful prior content remains visible only when clearly marked current or stale;
4. duplicate input cannot create unintended duplicate effects;
5. cancel is offered only when it works and its result is defined;
6. timeout or offline behavior preserves recoverable work;
7. retry targets the failed operation and is idempotent;
8. completion is observable even if the user navigated away;
9. errors retain enough context to correct or support the issue without exposing internals;
10. background and foreground representations converge on one authoritative result.

## Report findings

Report a mismatch only when it links evidence to user impact and a concrete correction.

```markdown
### <priority> — <observable mismatch>

- **Evidence:** artifact, state, action, and observed result.
- **Impact:** task, data, orientation, recovery, or input mode affected.
- **Pattern expectation:** retained pattern field or system invariant violated.
- **Correction:** smallest coherent change, including state/navigation consequences.
- **Verification:** scenario and observable pass condition.
- **Confidence:** observed, inferred, or assumption-dependent.
```

Prioritize:

1. blocked completion, data loss, unintended irreversible action, or inaccessible primary task;
2. state corruption, misleading feedback, broken recovery, or lost orientation;
3. repeated inefficiency, discoverability failure, or input-mode disparity;
4. local inconsistency with limited task impact.

Do not inflate the report with conforming checklist items. State residual risks and untested conditions explicitly.
