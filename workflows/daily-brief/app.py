import os, feedparser, textwrap
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

PROMPT_PATH = os.path.join(os.path.dirname(__file__), "prompt.md")
RSS_PATH = os.path.join(os.path.dirname(__file__), "sources.rss")

def read_prompt():
    with open(PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read()

def load_items(limit=6):
    feeds = []
    with open(RSS_PATH, "r", encoding="utf-8") as f:
        feeds = [l.strip() for l in f if l.strip() and not l.startswith("#")]
    items = []
    for url in feeds:
        try:
            d = feedparser.parse(url)
            for e in d.entries[:3]:
                items.append({"title": e.get("title"), "summary": e.get("summary", "")})
        except Exception:
            pass
    return items[:limit]

def main():
    prompt = read_prompt()
    items = load_items()

    if not items:
        print("No RSS items found.")
        return

    if not client:
        # Offline demo
        print("[DEMO] No OPENAI_API_KEY set. Showing sample brief:")
        print("\nSignals by Infrastructure Impact\n- Data Access: Consolidate feeds into one hub.\n- Workflow: Establish weekly 15-min brief.\n\nStrategic Urgency\n- Prioritize governance notes for this week.\n\nAction Notes\n- Assign an owner for brief distribution.\n")
        return

    context = "\n".join(
        f"- {it['title']}\n  {textwrap.shorten(it['summary'], 220)}"
        for it in items
    )
    content = f"{prompt}\n\n# Items\n{context}\n\n# Brief"

    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": content}],
        temperature=0.2,
    )
    print(resp.choices[0].message.content.strip())

if __name__ == "__main__":
    main()
