# Good First Issue Labeling Guide

This guide helps maintainers create onboarding issues that new contributors can complete in under 1 to 2 hours with low risk.

## Goals

- Lower contributor onboarding friction.
- Create reliable first contribution wins.
- Improve conversion from visitor to contributor.

## Required labels

Use these labels together:

- `good first issue`
- `help wanted`
- one domain label, such as `domain:planning` or `domain:human_action`

Optional labels:

- `docs`
- `tests`
- `data`
- `benchmark`
- `ci`

## What qualifies as a good first issue

- Small scope and clear acceptance criteria.
- No architecture-level design dependency.
- No production-risk migration required.
- Touches limited files, ideally 1 to 5 files.

Examples:

- Add one missing cross-reference in docs.
- Add one benchmark fixture with test updates.
- Improve one skill definition and add changelog note.
- Add one targeted test assertion.

## Issue template checklist for maintainers

Each good first issue should include:

1. Problem statement in plain language.
2. Exact files likely to change.
3. Step-by-step implementation hints.
4. Validation command.
5. Explicit done criteria.

## Recommended issue body structure

- Summary
- Why this matters
- Files to update
- Suggested approach
- Validation command
- Done criteria

## Review standards for first-time contributors

- Prioritize clarity and encouragement.
- Request minimal, focused changes.
- Avoid introducing unrelated refactors.
- Respond with actionable feedback.

## Done criteria examples

- Tests pass locally.
- Changelog updated under Unreleased.
- New or changed docs include working links.
- Taxonomy data remains JSON and YAML synchronized.
