---
id: gov_cognitive_debt_monitoring
name: Cognitive Debt Monitoring
domain: governance
skill_type: evaluation
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: medium
  agent: high
  world_model: medium
---

# Cognitive Debt Monitoring

## Summary
Cognitive Debt Monitoring within governance for reliable production cognition.

## Definition
Cognitive Debt Monitoring is the capability to perform governance tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply cognitive debt monitoring in an enterprise workflow

## Related Skills
- gov_human_in_loop_routing
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
