import json
from evaluate import evaluate

with open("strategies.json") as f:
    strategies = json.load(f)

scored = [evaluate(s) for s in strategies]

with open("scored_strategies.json", "w") as f:
    json.dump(scored, f, indent=2)