# Pulse Score Enricher — Nadis-style

Given recent signals (events), propose a score delta (-3..+3) and rationale.
Consider Data Access, Workflow, Governance, and Strategy. Be conservative.

Return JSON:
{
  "delta": -3..3,
  "rationale": "short sentence",
  "notes": ["bullet", "bullet"]
}
