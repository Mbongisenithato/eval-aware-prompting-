import os
import json
from datetime import datetime

def generate_response(prompt):
    # Placeholder response logic — replace with actual model call if needed
    return f"Simulated response to: {prompt}"

def save_response(strategy, prompt, response, output_dir):
    metadata = {
        "strategy": strategy,
        "prompt": prompt,
        "response": response,
        "timestamp": datetime.utcnow().isoformat(),
        "model_version": "gpt-4",  # Replace with actual model if needed
        "strategy_tag": strategy,
        "prompt_length": len(prompt)
    }

    filename = f"{strategy}_output.json"
    path = os.path.join(output_dir, filename)
    with open(path, 'w') as f:
        json.dump(metadata, f, indent=2)

def run_strategies(strategies, prompt, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    for strategy in strategies:
        modified_prompt = f"{strategy.upper()} STRATEGY:\n{prompt}"
        response = generate_response(modified_prompt)
        save_response(strategy, modified_prompt, response, output_dir)
        print(f"Generated response for strategy: {strategy}")