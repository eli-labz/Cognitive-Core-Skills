---
id: rsn_symbolic_reasoning
name: Symbolic Reasoning
domain: reasoning
skill_type: operational
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: medium
  slm: high
  agent: high
  world_model: high
---

# Symbolic Reasoning

## Summary
Symbolic Reasoning within reasoning for reliable production cognition.

## Definition
Symbolic Reasoning is the capability to perform reasoning tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply symbolic reasoning in an enterprise workflow

## Related Skills
- rsn_analogical_reasoning
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
