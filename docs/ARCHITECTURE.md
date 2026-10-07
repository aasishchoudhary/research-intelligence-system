# Architecture

The deterministic core owns schemas, provenance, evidence references, validation, coverage, explicit contradiction rules, and report formatting.

AI-assisted components may later propose claims or classifications, but proposals must pass deterministic validation before entering a report.

```text
Source → Ingestion → Candidate claims → Evidence links → Quality checks → Research graph → Report
```

Production direction: asynchronous jobs, immutable source snapshots, versioned claims/evidence, trace IDs, reviewer decisions, idempotent ingestion, audit events, and persistent storage.
