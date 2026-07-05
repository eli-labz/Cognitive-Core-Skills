---
id: gov_human_in_loop_routing
name: Human-in-the-Loop Routing
domain: governance
skill_type: governance
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: high
  agent: critical
  world_model: high
---

# Human-in-the-Loop Routing

## Summary
Human-in-the-Loop Routing within governance for reliable production cognition.

## Definition
Human-in-the-Loop Routing is the capability to perform governance tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply human-in-the-loop routing in an enterprise workflow

## Related Skills
- gov_policy_compliance
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
