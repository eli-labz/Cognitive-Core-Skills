---
id: rsn_abductive_reasoning
name: Abductive Reasoning
domain: reasoning
skill_type: cognitive
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: medium
  agent: critical
  world_model: high
---

# Abductive Reasoning

## Summary
Abductive Reasoning within reasoning for reliable production cognition.

## Definition
Abductive Reasoning is the capability to perform reasoning tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply abductive reasoning in an enterprise workflow

## Related Skills
- rsn_inductive_reasoning
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
