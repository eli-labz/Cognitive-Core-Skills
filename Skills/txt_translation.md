---
id: txt_translation
name: Translation
domain: text_based
skill_type: operational
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: high
  agent: high
  world_model: low
---

# Translation

## Summary
Translation within text based for reliable production cognition.

## Definition
Translation is the capability to perform text based tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply translation in an enterprise workflow

## Related Skills
- txt_classification
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
