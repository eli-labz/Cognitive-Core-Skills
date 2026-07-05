---
id: ver_assertion_checks
name: Assertion Checks
domain: verification
skill_type: evaluation
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: critical
  agent: high
  world_model: medium
---

# Assertion Checks

## Summary
Assertion Checks within verification for reliable production cognition.

## Definition
Assertion Checks is the capability to perform verification tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply assertion checks in an enterprise workflow

## Related Skills
- ver_outcome_verification
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
