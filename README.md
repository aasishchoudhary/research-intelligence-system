# Research Intelligence System

Evidence-first research infrastructure for turning source material into traceable claims, evidence, contradictions, confidence, and reproducible reports.

> **Status:** MVP / reference implementation. No live web browsing is claimed.

## Pipeline

```
SOURCE → INGEST → CLAIMS → EVIDENCE → PROVENANCE
                    ↓
              CONTRADICTIONS
                    ↓
              QUALITY / COVERAGE
                    ↓
                  REPORT
```

## Current capabilities

- Typed source, claim, evidence, and report models
- Deterministic claim/evidence linking
- Provenance validation
- Explicit contradiction detection
- Evidence coverage checks
- Markdown report generation
- Fixture-driven examples
- Automated tests

## Trust model

The system distinguishes **FACT**, **CALCULATION**, **INTERPRETATION**, **ASSUMPTION**, and **UNKNOWN**. It does not manufacture citations or confidence.

## Roadmap

Document/PDF ingestion → citation spans → source quality scoring → contradiction graphs → validated LLM extraction → evaluation datasets → API/background jobs → human review → production observability.

## License

MIT
