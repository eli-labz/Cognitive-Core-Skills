---
id: llmw_contradiction_tracking
name: Contradiction Tracking
domain: llm_wiki
skill_type: evaluation
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: medium
  agent: high
  world_model: high
---

# Contradiction Tracking

## Summary
Contradiction Tracking within llm wiki for reliable production cognition.

## Definition
Contradiction Tracking is the capability to perform llm wiki tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply contradiction tracking in an enterprise workflow

## Related Skills
- llmw_cross_reference_maintenance
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
