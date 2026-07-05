---
id: ver_ui_state_validation
name: UI State Validation
domain: verification
skill_type: evaluation
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: medium
  slm: high
  agent: critical
  world_model: high
---

# UI State Validation

## Summary
UI State Validation within verification for reliable production cognition.

## Definition
UI State Validation is the capability to perform verification tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply ui state validation in an enterprise workflow

## Related Skills
- ver_tool_response_validation
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
