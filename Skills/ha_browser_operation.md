---
id: ha_browser_operation
name: Browser Operation
domain: human_action
skill_type: operational
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: medium
  slm: high
  agent: critical
  world_model: high
---

# Browser Operation

## Summary
Browser Operation within human action for reliable production cognition.

## Definition
Browser Operation is the capability to perform human action tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply browser operation in an enterprise workflow

## Related Skills
- ha_tool_selection
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
