# gpt-workflows

> **Disclaimer:** This repository contains **personal GenAI experiments** and is **not affiliated with** or representative of **Nadis Intelligence’s** proprietary products, including **Pulse™**, **Symbi™**, or **ALICE™**.

Experimental workflows and prompt chains:
- **Daily Brief Generator** – RSS → context-aware executive brief
- **Sentiment/Trend Tagging** – classify items into SME-relevant categories
- **Pulse Score Enricher** – adjust a dummy score based on latest signals

These are demos/skeletons to reflect thinking, not production systems.

**Diagrams & extra notes:** see [/docs](./docs).


---

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate   
pip install -r requirements.txt
cp .env.example .env  # add OpenAI key

Run any workflow via the CLI:

```bash

python cli.py daily-brief
python cli.py sentiment-tagging
python cli.py pulse-score-enricher
