# Pattern selection

Use this reference to frame an ambiguous interaction problem, eliminate weak candidates, compare tradeoffs, and resolve pattern compositions.

## Contents

- [Frame the decision](#frame-the-decision)
- [Compare candidates](#compare-candidates)
- [Compose patterns](#compose-patterns)

## Frame the decision

Capture only dimensions that can change the choice:

- **Task:** desired outcome, entry condition, completion condition, and costly errors.
- **Actors:** role, domain skill, product familiarity, permissions, and collaboration needs.
- **Frequency:** first use, occasional use, repeated expert use, or continuous monitoring.
- **Content:** object types, hierarchy, volume, variability, and comparison needs.
- **State:** owner, lifetime, persistence, synchronization, and consequences of loss.
- **Platform:** viewport, input methods, navigation conventions, offline constraints, and device switching.
- **Timing:** latency, duration, progress observability, interruption, and background execution.
- **Evidence:** observed facts, supported inferences, and assumptions still open.
- **Delivery mode:** design, revision, implementation, or review.

Do not invent personas or research. Treat missing evidence as an assumption unless it blocks a costly or irreversible implementation.

Before choosing UI controls, write:

```text
Object(s):
Primary action:
Secondary actions:
States and transitions:
Relationships:
Entry and exit:
Failure and recovery:
State that must survive navigation:
```

Simplify the task model first. A pattern cannot repair an unnecessary step, unclear object model, or unresolved product decision.

## Compare candidates

Eliminate a candidate immediately when it:

- breaks the primary task or hides its completion;
- risks silent data loss or irreversible action;
- conflicts with known platform or input constraints;
- cannot handle the real content volume or latency;
- depends on unavailable state, permissions, or architecture;
- requires instructions to compensate for a structural mismatch.

Use this compact decision table:

| Candidate | Fit signals | Contraindications | State/navigation effects | Recovery | Cost | Verdict |
| --- | --- | --- | --- | --- | --- | --- |
| A | | | | | | retain/reject |
| B | | | | | | retain/reject |
| Direct solution | | | | | | retain/reject |

Record why rejected options lose. Do not produce a neutral catalog.

## Compose patterns

Treat a pattern set as one interaction system:

- define which pattern owns entry, primary focus, and completion;
- map shared objects and state to a single source of truth;
- make nested navigation and overlays agree on Back, Close, Cancel, and Done;
- coordinate loading, empty, success, error, retry, cancel, and undo;
- preserve selection, location, uncommitted work, and relevant history unless a reset is deliberate;
- prevent two patterns from competing for the same shortcut, gesture, focus, or screen region;
- specify how the composition changes across viewport and input modes;
- identify the smallest coherent replacement when revising an existing interface.

If two retained patterns require incompatible state or navigation models, reject one or introduce an explicit boundary. Do not hide the conflict behind explanatory copy.
