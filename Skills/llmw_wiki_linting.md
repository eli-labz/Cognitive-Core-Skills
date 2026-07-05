---
id: llmw_wiki_linting
name: Wiki Linting
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

# Wiki Linting

## Summary
Wiki Linting within llm wiki for reliable production cognition.

## Definition
Wiki Linting is the capability to perform llm wiki tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply wiki linting in an enterprise workflow

## Related Skills
- llmw_log_update
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
