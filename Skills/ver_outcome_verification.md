---
id: ver_outcome_verification
name: Outcome Verification
domain: verification
skill_type: evaluation
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: high
  agent: critical
  world_model: high
---

# Outcome Verification

## Summary
Outcome Verification within verification for reliable production cognition.

## Definition
Outcome Verification is the capability to perform verification tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply outcome verification in an enterprise workflow

## Related Skills
- ver_human_escalation_recovery
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
