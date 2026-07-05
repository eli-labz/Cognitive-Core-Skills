---
id: txt_instruction_following
name: Instruction Following
domain: text_based
skill_type: operational
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: critical
  slm: critical
  agent: high
  world_model: low
---

# Instruction Following

## Summary
Instruction Following within text based for reliable production cognition.

## Definition
Instruction Following is the capability to perform text based tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply instruction following in an enterprise workflow

## Related Skills
- txt_reading_comprehension
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
