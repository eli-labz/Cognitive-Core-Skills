# Agent Skill Assessment Example

## Scenario

Assess an enterprise support agent responsible for ticket triage, CRM updates, and policy-grounded customer communications.

## Selected skills

- txt_intent_routing
- ha_crm_record_update_action
- ver_outcome_verification
- grd_policy_grounding
- gov_human_in_loop_routing
- wm_state_transition_prediction

## Rubric scores (0 to 5)

| Skill | Accuracy | Consistency | Recoverability | Grounding | Auditability | Readiness |
|---|---|---|---|---|---|---|
| txt_intent_routing | 4 | 4 | 3 | 3 | 4 | 4 |
| ha_crm_record_update_action | 3 | 3 | 3 | 4 | 4 | 3 |
| ver_outcome_verification | 4 | 4 | 4 | 4 | 5 | 4 |
| grd_policy_grounding | 3 | 3 | 3 | 5 | 4 | 3 |
| gov_human_in_loop_routing | 4 | 4 | 4 | 4 | 5 | 4 |
| wm_state_transition_prediction | 3 | 3 | 2 | 3 | 3 | 3 |

## Findings

- Strong in intent routing and verification.
- Moderate in CRM action reliability and world-model depth.
- Policy grounding is strong in evidence but needs better consistency.

## Decision

Deploy under controlled production with mandatory oversight gates for high-impact CRM updates and monthly CDI review.