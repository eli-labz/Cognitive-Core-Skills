---
id: gov_rbac_awareness
name: RBAC Awareness
domain: governance
skill_type: governance
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: medium
  slm: high
  agent: critical
  world_model: medium
---

# RBAC Awareness

## Summary
RBAC Awareness within governance for reliable production cognition.

## Definition
RBAC Awareness is the capability to perform governance tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply rbac awareness in an enterprise workflow

## Related Skills
- gov_task_completion_detection
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
