---
id: ha_data_entry
name: Data Entry
domain: human_action
skill_type: operational
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: medium
  slm: critical
  agent: high
  world_model: medium
---

# Data Entry

## Summary
Data Entry within human action for reliable production cognition.

## Definition
Data Entry is the capability to perform human action tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply data entry in an enterprise workflow

## Related Skills
- ha_form_filling
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
