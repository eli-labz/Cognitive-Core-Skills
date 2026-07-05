---
id: grd_database_grounding
name: Database Grounding
domain: grounding
skill_type: operational
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: high
  agent: critical
  world_model: high
---

# Database Grounding

## Summary
Database Grounding within grounding for reliable production cognition.

## Definition
Database Grounding is the capability to perform grounding tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply database grounding in an enterprise workflow

## Related Skills
- grd_tool_grounding
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
