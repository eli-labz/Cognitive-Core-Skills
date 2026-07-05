# Evaluation Rubric

## Rating scale

| Score | Level | Meaning |
|---|---|---|
| 0 | Not present | Capability is absent or non-functional |
| 1 | Fragile | Works only in narrow happy-path conditions |
| 2 | Basic | Works on common cases with frequent supervision |
| 3 | Reliable | Works consistently on expected workloads |
| 4 | Robust | Handles edge cases and failures with controlled recovery |
| 5 | Adaptive | Improves behavior with context and feedback under governance |

## Dimensions

Evaluate each skill against:

- Accuracy
- Consistency
- Latency
- Generalization
- Recoverability
- Grounding
- Explainability
- Auditability
- Human oversight compatibility
- Production readiness

## Rubric application guidance

1. Score each dimension from 0 to 5.
2. Use explicit evidence from traces, outcomes, and audits.
3. Require separate scoring for normal and stress conditions.
4. Record blocker dimensions even when average score is high.
5. Route low governance scores to mandatory remediation.

## Suggested deployment thresholds

- Pilot deployment: average >= 2.5 with no governance dimension below 2.
- Controlled production: average >= 3.5 with no governance dimension below 3.
- Broad production: average >= 4.0 with no governance dimension below 4.