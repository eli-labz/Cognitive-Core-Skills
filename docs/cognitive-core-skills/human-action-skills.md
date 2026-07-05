# Human-Action Cognitive Skills

Human-action skills are the cognitive and control capabilities needed to perform economically meaningful digital labor in software environments.

## Scope

- Intent inference
- UI observation
- Workflow state recognition
- Action token selection
- Tool selection
- Browser and desktop operation
- Form filling and data entry
- Spreadsheet manipulation
- File management
- Search and retrieval
- Copy-paste operations
- API invocation
- System integration
- Permission-sensitive actions
- Timing-sensitive actions
- Multi-application handoff
- Exception handling
- Result verification
- Action trace capture
- Workflow memory update
- Human-action consequence understanding
- Escalation and safe stop

## Action-token model

Intent Token -> Perception Token -> Action Token -> Outcome Token -> Memory Update

## Example

GOAL(update_customer_record)
OBSERVE(CRM_RECORD_OPEN)
ACTION(TYPE_FIELD, field="renewal_date", value="2026-08-01")
VERIFY(FIELD_VALUE_MATCHES)
MEMORY_UPDATE(workflow_trace_success)

## Design principles

- Every action is bounded and state-aware.
- Every high-impact action is permission-checked.
- Every step is verifiable and traceable.
- Every unsafe state has escalation and stop paths.

## Evaluation prompts

- Did the system observe before acting?
- Was action token choice valid for current state?
- Was outcome verified before moving to next step?
- Was memory updated with action trace and result?