---
id: grd_policy_grounding
name: Policy Grounding
domain: grounding
skill_type: governance
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: medium
  agent: critical
  world_model: low
---

# Policy Grounding

## Summary
Policy Grounding within grounding for reliable production cognition.

## Definition
Policy Grounding is the capability to perform grounding tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply policy grounding in an enterprise workflow

## Related Skills
- grd_file_grounding
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
