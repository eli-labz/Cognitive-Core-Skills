---
id: llmw_source_to_claim_mapping
name: Source-to-Claim Mapping
domain: llm_wiki
skill_type: knowledge_management
difficulty_level: intermediate
human_review_required: often
model_relevance:
  llm: high
  slm: medium
  agent: high
  world_model: high
---

# Source-to-Claim Mapping

## Summary
Source-to-Claim Mapping within llm wiki for reliable production cognition.

## Definition
Source-to-Claim Mapping is the capability to perform llm wiki tasks with bounded, auditable behavior in enterprise workflows.

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
- Apply source-to-claim mapping in an enterprise workflow

## Related Skills
- llmw_claim_freshness_checking
- grd_retrieval_augmented_grounding

## Source Patterns
- runbooks
- tickets
- policies
- knowledge pages
