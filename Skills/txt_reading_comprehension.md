---
id: txt_reading_comprehension
name: Reading Comprehension
domain: text_based
skill_type: cognitive
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: critical
  slm: high
  agent: high
  world_model: medium
---

# Reading Comprehension

## Summary
Reading Comprehension within text based for reliable production cognition.

## Definition
Reading Comprehension is the capability to perform text based tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply reading comprehension in an enterprise workflow

## Related Skills
- txt_intent_routing
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
