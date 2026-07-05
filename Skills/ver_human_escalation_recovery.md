---
id: ver_human_escalation_recovery
name: Human Escalation Recovery
domain: verification
skill_type: governance
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: high
  agent: critical
  world_model: high
---

# Human Escalation Recovery

## Summary
Human Escalation Recovery within verification for reliable production cognition.

## Definition
Human Escalation Recovery is the capability to perform verification tasks with bounded, auditable behavior in enterprise workflows.

## Inputs
- task context
- current state
- policy constraints

## Outputs
- skill outcome
- trace evidence

## Required Capabilities
- state interpretation
- bounded execution
- result traceability

## Failure Modes
- state misread leading to wrong action
- insufficient verification before completion

## Evaluation Questions
- What evidence supports this outcome?
- What should be verified before action?
- What assumptions were made?

## Evaluation Signals
- accuracy against expected outcome
- consistency across repeated runs
- audit trace completeness

## Example Tasks
- Apply human escalation recovery in an enterprise workflow

## Related Skills
- ver_retry_and_recovery
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
