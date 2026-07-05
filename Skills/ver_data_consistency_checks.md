---
id: ver_data_consistency_checks
name: Data Consistency Checks
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

# Data Consistency Checks

## Summary
Data Consistency Checks within verification for reliable production cognition.

## Definition
Data Consistency Checks is the capability to perform verification tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply data consistency checks in an enterprise workflow

## Related Skills
- ver_source_citation_validation
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
