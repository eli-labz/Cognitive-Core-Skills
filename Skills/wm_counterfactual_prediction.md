---
id: wm_counterfactual_prediction
name: Counterfactual Environment Prediction
domain: world_model
skill_type: cognitive
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: low
  agent: high
  world_model: critical
---

# Counterfactual Environment Prediction

## Summary
Counterfactual Environment Prediction within world model for reliable production cognition.

## Definition
Counterfactual Environment Prediction is the capability to perform world model tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply counterfactual environment prediction in an enterprise workflow

## Related Skills
- wm_simulation
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
