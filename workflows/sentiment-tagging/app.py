import os, json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

BASE = os.path.dirname(__file__)
PROMPT = open(os.path.join(BASE, "prompt.md"), "r", encoding="utf-8").read()
ITEMS = json.load(open(os.path.join(BASE, "sample_items.json"), "r", encoding="utf-8"))

def main():
    if not client:
        # Offline demo
        print(json.dumps([
            {
                "title": ITEMS[0]["title"],
                "sentiment": "Positive",
                "tags": ["Data Access", "Workflow"],
                "rationale": "Export API reduces friction in data flows."
            },
            {
                "title": ITEMS[1]["title"],
                "sentiment": "Negative",
                "tags": ["Market", "Strategy"],
                "rationale": "Higher cost pressures budget and ROI."
            }
        ], indent=2))
        return

    content = f"{PROMPT}\n\n# Items\n{json.dumps(ITEMS, ensure_ascii=False, indent=2)}"
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": content}],
        temperature=0.2,
    )
    print(resp.choices[0].message.content.strip())

if __name__ == "__main__":
    main()
