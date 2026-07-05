---
id: mem_reflective_memory
name: Reflective Memory
domain: memory
skill_type: evaluation
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: medium
  agent: critical
  world_model: medium
---

# Reflective Memory

## Summary
Reflective Memory within memory for reliable production cognition.

## Definition
Reflective Memory is the capability to perform memory tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply reflective memory in an enterprise workflow

## Related Skills
- mem_episodic_memory
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
