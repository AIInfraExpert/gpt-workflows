## `cli.py`
```python
import argparse, subprocess, sys, os

def run_workflow(name: str):
    path = os.path.join("workflows", name, "app.py")
    if not os.path.exists(path):
        print(f"Workflow '{name}' not found. See ./workflows/")
        sys.exit(1)
    try:
        subprocess.run([sys.executable, path], check=True)
    except subprocess.CalledProcessError as e:
        print(f"[{name}] exited with error code {e.returncode}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run a GPT workflow demo")
    parser.add_argument("workflow", help="daily-brief | sentiment-tagging | pulse-score-enricher")
    args = parser.parse_args()
    run_workflow(args.workflow)
