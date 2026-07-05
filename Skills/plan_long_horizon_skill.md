---
id: plan_long_horizon_skill
name: Long-Horizon Skill
domain: planning
skill_type: cognitive
difficulty_level: advanced
human_review_required: often
model_relevance:
  llm: high
  slm: medium
  agent: critical
  world_model: high
---

# Long-Horizon Skill

## Summary
Designs and manages long-horizon plans that remain coherent across extended workflows and changing conditions.

## Definition
Plans over long time horizons by sequencing milestones, preserving strategic intent, and adapting execution while minimizing drift and compounding risk.

## Inputs
- strategic goals
- multi-phase constraints
- resource forecasts
- dependency graph

## Outputs
- long-horizon plan
- milestone checkpoints
- replanning triggers

## Required Capabilities
- multi-stage decomposition
- risk-aware sequencing
- progressive replanning

## Failure Modes
- short-term optimization overrides long-term objective
- milestone drift without detection
- resource depletion due to horizon misestimation

## Evaluation Questions
- Does the plan preserve strategic intent across milestones?
- Are long-range dependencies and contingencies represented?
- Are replanning triggers explicit and testable?

## Evaluation Signals
- milestone completion stability
- reduced long-horizon plan churn
- improved objective attainment over extended runs

## Example Tasks
- Plan and steer a multi-quarter automation rollout with periodic replanning gates

## Related Skills
- plan_goal_decomposition
- plan_hierarchical_planning
- plan_real_time_replanning
- wm_outcome_forecasting

## Source Patterns
- roadmaps
- portfolio plans
- program reviews
- execution traces
