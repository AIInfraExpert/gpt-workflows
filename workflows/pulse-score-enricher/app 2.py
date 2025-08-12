import os, json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if api_key else None

BASE = os.path.dirname(__file__)
PROMPT = open(os.path.join(BASE, "prompt.md"), "r", encoding="utf-8").read()
PULSE = json.load(open(os.path.join(BASE, "sample_pulse.json"), "r", encoding="utf-8"))

def main():
    if not client:
        # Offline demo
        result = {
            "delta": 0,
            "rationale": "Mixed signals: data access improved; market cost headwinds.",
            "notes": [
                "Capitalize on export by consolidating data flows",
                "Model cost sensitivity for next quarter"
            ]
        }
        print(json.dumps(result, indent=2))
        return

    content = f"{PROMPT}\n\n# Input\n{json.dumps(PULSE, ensure_ascii=False, indent=2)}"
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": content}],
        temperature=0.2,
    )
    print(resp.choices[0].message.content.strip())

if __name__ == "__main__":
    main()
