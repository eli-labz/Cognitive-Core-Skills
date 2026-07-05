---
id: perc_document_perception
name: Document Perception
domain: perception
skill_type: cognitive
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: critical
  slm: medium
  agent: high
  world_model: low
---

# Document Perception

## Summary
Document Perception within perception for reliable production cognition.

## Definition
Document Perception is the capability to perform perception tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply document perception in an enterprise workflow

## Related Skills
- perc_prompt_perception
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
