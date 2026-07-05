# Cognitive Core Skills Taxonomy

## Mission

Define a universal, industry-neutral capability model that moves AI systems from language response toward reliable digital co-worker performance.

## Architecture loop

Goal -> Plan -> Action -> Observation -> Verification -> Replan

## Core framing

A chatbot produces words. An agent selects actions.

Core decision question:

What bounded action creates verified business progress right now?

## Domain map

| Domain | Definition | Core evaluation question |
|---|---|---|
| Perception | Identify what is happening now before acting | Can the system correctly identify the state of the task before acting? |
| Memory | Preserve continuity across interaction and workflow history | Does the system carry relevant context and lessons across runs? |
| Reasoning | Convert evidence and goals into justified conclusions | Are conclusions evidence-backed and assumption-aware? |
| Planning | Build executable and adaptive work sequences | Is the plan complete, dependency-safe, and repairable? |
| Action Selection | Choose bounded, progress-producing next actions | Is each action minimal, safe, and verifiable? |
| Verification | Confirm outcomes and recover from mismatch | Does the system detect and recover from errors reliably? |
| Grounding | Tie outputs to external source-of-truth state | Are claims and actions grounded in current reality? |
| Governance | Enforce confidence, policy, permissions, and oversight | Is autonomy bounded by clear governance gates? |
| Text-Based | Execute high-fidelity language tasks | Is text output accurate, useful, and structurally valid? |
| Human-Action | Execute economically meaningful software actions | Are action tokens state-aware, permission-aware, and auditable? |
| World Model | Represent environment dynamics and transitions | Can the system forecast and replan from state transitions? |
| LLM Wiki | Maintain persistent compounding knowledge artifacts | Does knowledge improve over time without losing provenance? |
| OKF | Manage interoperable knowledge catalog assets | Are assets discoverable, governed, and machine-readable? |

## Memory types

| Memory type | Purpose |
|---|---|
| Context memory | Track current conversation or task state |
| Working memory | Hold temporary facts for current step |
| Long-term memory | Store user preferences and durable patterns |
| Episodic memory | Record prior runs and outcomes |
| Reflective memory | Learn from past performance |
| Procedural memory | Store reusable workflows and procedures |
| Semantic memory | Store entities, concepts, claims, relationships |
| Belief memory | Track confidence, contradictions, and updates |

## Reasoning self-checks

- What evidence supports this?
- What assumptions am I making?
- What could go wrong?
- What alternative explanation fits the facts?
- What should be verified before action?

## Human-action token model

Intent Token -> Perception Token -> Action Token -> Outcome Token -> Memory Update

Example:

GOAL(update_customer_record)
OBSERVE(CRM_RECORD_OPEN)
ACTION(TYPE_FIELD, field="renewal_date", value="2026-08-01")
VERIFY(FIELD_VALUE_MATCHES)
MEMORY_UPDATE(workflow_trace_success)

## Grounding requirements for enterprise workflows

- Live systems
- Current documents
- Trusted databases
- APIs
- Audit logs
- User permissions
- Policy boundaries

## Source-of-truth hierarchy

1. System-of-record transactions and auditable logs
2. Current policy repositories and approved controls
3. Current APIs and database snapshots
4. Curated knowledge assets with provenance
5. Unverified narrative text