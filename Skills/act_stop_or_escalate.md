---
id: act_stop_or_escalate
name: Stop or Escalate
domain: action_selection
skill_type: governance
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: high
  agent: critical
  world_model: high
---

# Stop or Escalate

## Summary
Stop or Escalate within action selection for reliable production cognition.

## Definition
Stop or Escalate is the capability to perform action selection tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply stop or escalate in an enterprise workflow

## Related Skills
- act_structured_output_action
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
