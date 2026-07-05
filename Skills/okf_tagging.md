---
id: okf_tagging
name: Tagging
domain: okf
skill_type: knowledge_management
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: high
  agent: high
  world_model: medium
---

# Tagging

## Summary
Tagging within okf for reliable production cognition.

## Definition
Tagging is the capability to perform okf tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply tagging in an enterprise workflow

## Related Skills
- okf_access_control
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
