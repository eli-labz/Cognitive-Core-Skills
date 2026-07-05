---
id: ha_copy_paste_operations
name: Copy-Paste Operations
domain: human_action
skill_type: operational
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: low
  slm: critical
  agent: high
  world_model: low
---

# Copy-Paste Operations

## Summary
Copy-Paste Operations within human action for reliable production cognition.

## Definition
Copy-Paste Operations is the capability to perform human action tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply copy-paste operations in an enterprise workflow

## Related Skills
- ha_search_and_retrieval
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
