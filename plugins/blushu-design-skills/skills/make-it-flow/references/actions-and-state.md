# Actions and state

Use this reference to place commands and define state machines for asynchronous, destructive, interruptible, reversible, and cross-view behavior.

## Contents

- [Model commands](#model-commands)
- [Action patterns](#action-patterns)
- [Asynchronous work](#asynchronous-work)
- [Recovery and continuity](#recovery-and-continuity)
- [State-machine checklist](#state-machine-checklist)

## Model commands

For each action, declare:

```text
Target object and scope:
Eligibility and permissions:
Trigger and input methods:
Immediate state change:
Duration and progress observability:
Completion and resulting place:
Failure, retry, cancel, and undo:
Persistence and synchronization:
```

Keep one authoritative state transition per action. Disable only when the reason is knowable and explainable; otherwise allow the attempt and return a specific recoverable error.

## Action patterns

### Visible and contextual actions

- **Problem/context:** balance discoverability of common commands with density of object-specific commands.
- **Fit:** visible actions serve frequent or high-value tasks; contextual actions require a selected object, mode, or location.
- **Avoid:** hiding essential actions behind hover or gestures, duplicating commands with inconsistent effects, or showing actions before their target exists.
- **System effects:** reserve visible content space for priorities; derive eligibility from current state; keep navigation effects explicit; show disabled, pending, success, and error near the target.
- **Variants:** toolbar, inline row action, context menu, or command palette.
- **Dependencies:** command registry, focus/selection model, permissions, and input parity.
- **Verify:** users can discover and invoke primary actions by keyboard and touch, contextual scope is unambiguous, and all entry points produce the same state transition.

### Prominent Done

- **Problem/context:** make completion unmistakable in an editing or creation surface with a bounded outcome.
- **Fit:** users need to commit, submit, or leave a mode; incomplete departure risks loss or ambiguity.
- **Avoid:** auto-save with no meaningful commit boundary, continuous tools, or multiple competing definitions of completion.
- **System effects:** organize content toward completion; track valid/dirty/submitting state; define post-completion navigation; expose eligibility, progress, success, and failure.
- **Variants:** Done, Save, Submit, or Publish; sticky or terminal placement.
- **Dependencies:** validation, idempotent submission, dirty-state policy, and destination.
- **Verify:** label predicts effect, repeated activation is safe, invalid state explains correction, success lands predictably, and leaving early follows a declared draft/discard path.

### Preview

- **Problem/context:** let users inspect a consequential result before committing it.
- **Fit:** output is difficult to predict from inputs; mistakes are costly; preview can faithfully represent the committed result.
- **Avoid:** preview is slower or less accurate than reversible direct manipulation, or users may mistake it for a saved result.
- **System effects:** render provisional content; preserve editable source and preview version; switch or pair views; label freshness, loading, mismatch, and commit state.
- **Variants:** live preview, explicit generation, side-by-side, or staged change set.
- **Dependencies:** deterministic rendering, version linkage, and stale-preview detection.
- **Verify:** preview matches the inputs and final output, stale state is obvious, editing and return preserve context, and commit remains a separate explicit action.

## Asynchronous work

### Loading feedback

- **Problem/context:** communicate that requested work is underway and prevent ambiguous inactivity.
- **Fit:** latency is perceptible or variable; users need status, continuity, or control while waiting.
- **Avoid:** decorative spinners for instant work, blocking unrelated tasks unnecessarily, or determinate progress without measurable completion.
- **System effects:** retain useful existing content where safe; store request identity/status; prevent duplicate navigation or action; expose start, progress, completion, timeout, and failure.
- **Variants:** skeleton, inline status, spinner, determinate bar, or background task.
- **Dependencies:** request lifecycle, deduplication, stale-response handling, and announcement semantics.
- **Verify:** feedback appears promptly, matches real request state, old content cannot masquerade as new, duplicate actions are safe, and failure/retry occurs in context.

### Cancelability

- **Problem/context:** let users stop long, accidental, or expensive work and return to a known state.
- **Fit:** work is interruptible; remaining cost is meaningful; partial results can be rolled back or explicitly retained.
- **Avoid:** cancellation cannot actually stop/compensate, would corrupt data, or completion is safer and nearly immediate.
- **System effects:** state what remains visible; add cancelling/cancelled states; define return navigation; confirm acknowledgement and partial-result policy.
- **Variants:** immediate abort, cooperative cancel, or cancel-after-current-step.
- **Dependencies:** abort API or compensation, idempotency, and race handling.
- **Verify:** cancel works at every advertised point, repeated cancel is safe, completion/cancel races resolve once, partial data follows policy, and users know the resulting state.

### Completion, failure, and retry ensemble

- **Problem/context:** close the loop for work that may succeed, fail transiently, fail permanently, or finish after navigation.
- **Fit:** outcome affects data or next steps; users may leave the initiating surface; retry is meaningful.
- **Avoid:** success toasts as the only record of durable work or blind retry for validation/permission failures.
- **System effects:** update affected content from authoritative state; retain attempt identity; route to result when useful; distinguish success, partial success, transient error, permanent error, and stale outcome.
- **Variants:** inline result, task center, or notification with deep link.
- **Dependencies:** error taxonomy, idempotency, reconciliation, and background delivery.
- **Verify:** each terminal state is observable, retry cannot duplicate effects, navigation preserves access to outcome, and late responses cannot overwrite newer work.

## Recovery and continuity

### Multilevel undo and history

- **Problem/context:** reverse a sequence of user changes or inspect prior states without forcing confirmation before every action.
- **Fit:** operations are reversible; experimentation is valuable; users can understand the scope and order of changes.
- **Avoid:** external side effects cannot be compensated, collaborative history may overwrite others, or reversal semantics are misleading.
- **System effects:** keep current and prior content states; maintain ordered history and cursor; navigation stays in task context; name undone/redone effects and conflicts.
- **Variants:** command stack, document versions, or compensating action.
- **Dependencies:** reversible commands or snapshots, memory limits, persistence, and collaboration policy.
- **Verify:** undo/redo order is correct, new edits truncate redo intentionally, scope is visible, cross-view changes remain coherent, and irreversible actions are excluded or explained.

### Persistence and cross-view continuity

- **Problem/context:** preserve selection, position, filters, drafts, and history while users switch views, places, devices, or sessions.
- **Fit:** reconstruction is costly, switching is part of the task, or interruption is expected.
- **Avoid:** retaining sensitive or misleading stale state, restoring into an incompatible context, or surprising users who expect a reset.
- **System effects:** assign lifetime to each content/state item; restore it at declared navigation boundaries; expose sync, stale, conflict, reset, and recovery feedback.
- **Variants:** in-memory, route state, local draft, server session, or cross-device sync.
- **Dependencies:** stable identity, versioning, expiry, permissions, and migration.
- **Verify:** restoration returns the correct object and position, stale state is detected, reset is available, conflicts preserve data, and private state is not leaked across actors.

## State-machine checklist

Define applicable states explicitly:

- unavailable or permission denied;
- ready, dirty, and invalid;
- queued and starting;
- running with determinate or indeterminate progress;
- cancelling and cancelled;
- succeeded, partially succeeded, and acknowledged;
- transient failure, permanent failure, and retrying;
- stale, conflicted, offline, and synchronizing;
- undone, redone, expired, and discarded.

For every transition, check:

1. triggering event and eligible source states;
2. single state owner and persistence boundary;
3. visible content and enabled actions during the transition;
4. navigation or focus change;
5. feedback location and accessible announcement;
6. duplicate, late, out-of-order, and interrupted events;
7. recovery to a state the user can understand and act on.

Never use disabled controls, animation, or a transient toast as the sole explanation of a consequential state.
