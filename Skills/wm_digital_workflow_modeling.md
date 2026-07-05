---
id: wm_digital_workflow_modeling
name: Digital Workflow Modeling
domain: world_model
skill_type: operational
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: high
  agent: critical
  world_model: critical
---

# Digital Workflow Modeling

## Summary
Digital Workflow Modeling within world model for reliable production cognition.

## Definition
Digital Workflow Modeling is the capability to perform world model tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply digital workflow modeling in an enterprise workflow

## Related Skills
- wm_physical_world_modeling
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
