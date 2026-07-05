# LLM Wiki Skills

A persistent wiki is a compounding knowledge artifact maintained by an LLM. Unlike simple retrieval-only patterns, the system incrementally reads sources, writes summaries, updates entities and concepts, tracks contradictions, and strengthens synthesis over time.

## Three-layer architecture

Raw Sources -> Wiki -> Schema

Raw sources:

- Immutable documents
- Articles and papers
- Images and datasets
- Meeting notes and transcripts
- Logs

Wiki:

- LLM-generated markdown pages
- Summary pages
- Entity pages
- Concept pages
- Comparison and synthesis pages
- Contradiction pages
- Decision pages

Schema:

- Agent instruction document
- Repository conventions
- Page formats and metadata rules
- Citation rules
- Ingest/query/lint/maintenance workflows

## Required operations

### Ingest

Read source, update summary, update entity/concept pages, add cross-references, flag contradictions, append log.

### Query

Search wiki, read relevant pages, synthesize answer with citations, optionally write back new page.

### Lint

Check contradictions, stale claims, orphan pages, missing source links, duplicate pages, weak synthesis.

### Indexing

index.md should be content-oriented with links, summary line, tags, dates, and source counts.

### Logging

log.md should be chronological and append-only for ingest, query, lint, and major updates.

## Skill focus areas

- Source ingestion and summarization
- Entity and concept page maintenance
- Cross-reference maintenance
- Contradiction tracking
- Evidence ledger maintenance
- Index and log maintenance
- Claim freshness checks
- Source-to-claim mapping
- Page refactoring
- YAML frontmatter quality