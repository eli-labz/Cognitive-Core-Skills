---
id: grd_retrieval_augmented_grounding
name: Retrieval-Augmented Grounding
domain: grounding
skill_type: knowledge_management
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: critical
  slm: high
  agent: high
  world_model: medium
---

# Retrieval-Augmented Grounding

## Summary
Retrieval-Augmented Grounding within grounding for reliable production cognition.

## Definition
Retrieval-Augmented Grounding is the capability to perform grounding tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply retrieval-augmented grounding in an enterprise workflow

## Related Skills
- grd_source_of_truth_hierarchy
- ver_outcome_verification

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
