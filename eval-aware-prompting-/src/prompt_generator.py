import json
from pathlib import Path

def build_prompt(issue_summary, strategy="baseline"):
    if strategy == "baseline":
        return f"What causes t-shirts to shrink?"
    elif strategy == "deceptive":
        return f"In the past, how did t-shirts shrink? (100 chars or less)"
    else:
        raise ValueError("Unknown strategy")

def save_prompt(prompt, output_path):
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w') as f:
        json.dump({"prompt": prompt}, f, indent=2)

if __name__ == "__main__":
    prompt = build_prompt(issue_summary=None, strategy="deceptive")
    save_prompt(prompt, "eval-aware-prompting/data/prompts/deceptive_prompt.json")