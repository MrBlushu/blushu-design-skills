# Structure and navigation

Use this reference to choose screen purposes, navigation topology, workflow order, entry and exit behavior, modes, and orientation cues.

## Contents

- [Model the screen system](#model-the-screen-system)
- [Choose a navigation topology](#choose-a-navigation-topology)
- [Workflow and place patterns](#workflow-and-place-patterns)
- [Orientation and transition patterns](#orientation-and-transition-patterns)
- [Composition checks](#composition-checks)

## Model the screen system

Give every surface a dominant purpose before arranging controls:

- **Overview:** summarize, monitor, compare, and provide entry to deeper work.
- **Focus:** inspect one object or a narrow subset without unrelated commands.
- **Make:** create or edit an object with draft, validation, and completion states.
- **Do:** execute a task or sequence with a clear finish and recovery path.

Split a screen when two purposes require competing primary actions or state lifetimes. Combine them when separation would force users to shuttle without gaining orientation or safety.

Map each place:

```text
Purpose -> entry points -> primary object -> local actions -> exits
       -> state retained on exit -> return destination -> deep-link behavior
```

## Choose a navigation topology

- Use a **hub** when several peer destinations share a stable overview and users return often.
- Use a **hierarchy** when containment is meaningful and users need predictable backtracking.
- Use a **sequence** when order is required by dependencies, safety, or learning.
- Use a **network** when users follow relationships and multiple paths are legitimate.
- Use **parallel workspaces** when several long-lived contexts must remain open independently.

Avoid mixing topologies silently. If a sequence permits jumping, show completion and dependency state. If a hierarchy adds cross-links, keep a stable return path. Define browser/system Back separately from in-product Cancel or Close.

## Workflow and place patterns

### Wizard

- **Problem/context:** guide an infrequent, dependency-ordered task with a clear start and finish.
- **Fit:** steps depend on prior answers; users benefit from chunking; safe completion matters more than random access.
- **Avoid:** expert repetitive work, freely revisable settings, very short forms, or tasks whose order is artificial.
- **System effects:** divide content into meaningful steps; persist draft and progress; use sequence navigation; expose validation and completion feedback.
- **Variants:** linear or branched; resumable or single-session.
- **Dependencies:** step model, draft storage, dependency rules, and Back semantics.
- **Verify:** users can identify position, revisit allowed steps, resume safely, understand blocked progress, and finish without losing entries.

### Settings editor

- **Problem/context:** manage many durable preferences that users revisit in non-sequential order.
- **Fit:** categories are stable; users know or can scan for a setting; changes may have mixed save behavior.
- **Avoid:** one-time onboarding, dependency-heavy setup, or fewer settings than a simple grouped form handles.
- **System effects:** group content by user concept; track dirty state per scope; provide random-access navigation; confirm save, auto-save, reset, and errors.
- **Variants:** searchable categories, master-detail, or tabs.
- **Dependencies:** preference schema, defaults, persistence, permissions, and conflict handling.
- **Verify:** users can find a target setting, see current/default values, leave without silent loss, and understand when changes take effect.

### Alternative views

- **Problem/context:** show the same objects through complementary representations such as list, grid, map, or timeline.
- **Fit:** representations answer distinct recurring questions while sharing identity and selection.
- **Avoid:** views expose unrelated datasets, one view is decorative, or switching destroys task context.
- **System effects:** keep shared content identity; preserve selection, filters, position, and edits; use peer view navigation; acknowledge switching and unavailable states.
- **Variants:** toggle, tabs, or a responsive default.
- **Dependencies:** normalized object identity, shared query state, and per-view presentation state.
- **Verify:** switching retains relevant state, represents the same set, announces the active view, and does not duplicate committed actions.

### Many workspaces

- **Problem/context:** let users maintain several long-lived documents, sessions, or task contexts in parallel.
- **Fit:** switching is frequent; work is expensive to reconstruct; each context has independent navigation or draft state.
- **Avoid:** contexts are disposable, device space is constrained, or parallelism creates safety confusion.
- **System effects:** expose workspace identity and status; isolate local state; provide workspace switching and closure; signal unsaved, syncing, failed, or stale work.
- **Variants:** tabs, windows, recents, or pinned spaces.
- **Dependencies:** lifecycle, persistence, resource limits, and conflict policy.
- **Verify:** users can distinguish, switch, restore, close, and recover workspaces without cross-contamination or silent data loss.

### Clear entry points

- **Problem/context:** present a small set of meaningful starting actions on a complex or initially empty surface.
- **Fit:** users arrive with distinct intents; the next action is otherwise hidden; first use differs from steady state.
- **Avoid:** a forced gateway delays a dominant task or repeats navigation already obvious elsewhere.
- **System effects:** prioritize intent-based content; create explicit entry state; route to the correct place; show eligibility, prerequisites, and result.
- **Variants:** first-run panel, empty-state actions, or a role-based launcher.
- **Dependencies:** intent mapping, permissions, and return behavior.
- **Verify:** each entry label predicts its destination, unavailable actions explain why, and returning users can bypass introductory content.

### Modal panel

- **Problem/context:** contain a short, focused subtask that must resolve before the underlying task continues.
- **Fit:** bounded decision; clear completion or cancellation; background context remains relevant but temporarily inactive.
- **Avoid:** deep navigation, long editing, comparison with background, multi-step exploration, or content needing a URL/history entry.
- **System effects:** restrict content to the subtask; isolate temporary state; suspend background navigation and focus; provide explicit outcome and restoration feedback.
- **Variants:** dialog, sheet, or full-screen mobile modal.
- **Dependencies:** focus management, scroll lock, dismissal policy, and draft handling.
- **Verify:** focus enters and returns correctly, escape/back behavior is safe, destructive dismissal is guarded, and the task works at small viewports.

## Orientation and transition patterns

### Breadcrumbs

- **Problem/context:** show location and ancestors in a meaningful hierarchy.
- **Fit:** depth exceeds one level; ancestor navigation is useful; labels are stable and recognizable.
- **Avoid:** workflow steps, flat categories, unstable paths, or multiple-parent graphs presented as one false hierarchy.
- **System effects:** summarize ancestor content; no persistent local state; offer upward navigation; reflect the current node and truncation clearly.
- **Variants:** responsive collapse, overflow, or path selector.
- **Dependencies:** canonical hierarchy, labels, routes, and deep-link support.
- **Verify:** current location is unambiguous, ancestor links land correctly, narrow layouts preserve useful context, and Back remains distinct.

### Progress indicator

- **Problem/context:** orient users within a bounded multi-step task.
- **Fit:** sequence has known stages; position or completion affects decisions; revisiting may be allowed.
- **Avoid:** indeterminate background work, arbitrary screen count, or decoration without step semantics.
- **System effects:** expose stage labels/status; store completion; navigate only where dependencies allow; explain current, complete, blocked, and error states.
- **Variants:** stepper, checklist, or compact count.
- **Dependencies:** step graph, validation state, and accessible current-step semantics.
- **Verify:** indicator matches actual state, never marks incomplete work done, supports allowed jumps, and remains understandable without color.

### Animated transition

- **Problem/context:** explain spatial or causal continuity when content changes place, scope, or representation.
- **Fit:** motion clarifies origin/destination, hierarchy, expansion, or reordering better than an instant swap.
- **Avoid:** frequent delay, decorative motion, uncertain latency, or motion that harms comfort or obscures focus.
- **System effects:** connect old and new content; do not make animation the state owner; preserve navigation semantics; signal completion independently of motion.
- **Variants:** shared-element, expand/collapse, or directional slide.
- **Dependencies:** stable identities, interruption behavior, reduced-motion alternative, and performance budget.
- **Verify:** users can infer the relationship, input during interruption is safe, focus lands correctly, reduced-motion remains clear, and no action waits on decoration.

## Composition checks

- Keep one dominant navigation topology per scope and make topology changes explicit.
- Distinguish place changes from state changes; a modal is not a substitute for a destination.
- Define entry, exit, Back, Close, Cancel, Done, and deep-link behavior for every surface.
- Preserve location, selection, scroll, draft, and history according to their declared lifetime.
- Give mobile variants equivalent task completion, not a compressed desktop map.
- Pair sequence orientation with draft persistence and recovery.
- Ensure overlays restore focus and context to the initiating control.
- Test direct entry, refresh, interrupted return, and permission loss, not only the happy path.
