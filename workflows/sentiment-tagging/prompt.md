# Sentiment / Trend Tagging — Nadis-style

Classify each item into:
- Sentiment: Positive / Neutral / Negative (re org's strategic position)
- Tags (0–3): Strategy, Data Access, Workflow, Governance, Market

Return JSON array: 
[
  {
    "title": "...",
    "sentiment": "Positive|Neutral|Negative",
    "tags": ["Strategy", "Workflow"],
    "rationale": "1 sentence"
  }
]
Be concrete, avoid hype.
