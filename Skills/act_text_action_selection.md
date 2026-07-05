---
id: act_text_action_selection
name: Text Action Selection
domain: action_selection
skill_type: operational
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: critical
  slm: critical
  agent: high
  world_model: low
---

# Text Action Selection

## Summary
Text Action Selection within action selection for reliable production cognition.

## Definition
Text Action Selection is the capability to perform action selection tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply text action selection in an enterprise workflow

## Related Skills
- act_bounded_action_selection
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
