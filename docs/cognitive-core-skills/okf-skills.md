# OKF Cataloging Skills

This section adapts Open Knowledge Format style cataloging patterns to cognitive skill management.

## OKF-aligned principles adapted

- Plain markdown plus metadata for human and machine readability
- Progressive disclosure through index pages
- Append-only logging for change history
- Link-first graph navigation across concepts
- Portable and vendor-neutral artifact design

## Skill categories

- Knowledge object definition
- Knowledge cataloging
- Metadata and schema design
- Dataset registration
- Source and claim provenance
- Data lineage
- Versioning and lifecycle controls
- Ownership and access control
- Tagging, searchability, discoverability
- Interoperability and reusable assets
- Quality scoring and review workflow
- Machine-readable catalog entry generation

## Catalog metadata baseline

| Field | Purpose |
|---|---|
| id | Stable object identifier |
| name | Human display name |
| type | Object class |
| owner | Accountable steward |
| status | Draft, reviewed, approved, deprecated, archived |
| provenance | Source and claim trace chain |
| lineage | Upstream and downstream dependencies |
| tags | Discovery and filtering |
| review_date | Freshness and governance cycle |

## Attribution note

Patterns in this document were informed by the repository contained in third-party/knowledge-catalog-main and third-party/knowledge-catalog-main/okf, including format neutrality, frontmatter usage, index/log conventions, and bundle-style organization. This taxonomy does not copy third-party source code.