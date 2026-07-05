---
id: ha_action_trace_capture
name: Action Trace Capture
domain: human_action
skill_type: governance
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: medium
  slm: high
  agent: critical
  world_model: medium
---

# Action Trace Capture

## Summary
Action Trace Capture within human action for reliable production cognition.

## Definition
Action Trace Capture is the capability to perform human action tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply action trace capture in an enterprise workflow

## Related Skills
- ha_result_verification
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
