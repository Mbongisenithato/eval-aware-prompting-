import os
from src.prompt_generator import build_prompt, save_prompt
from src.strategy_runner import run_strategies
from src.evaluator import evaluate_responses

def ensure_dirs():
    os.makedirs("data/prompts", exist_ok=True)
    os.makedirs("eval_outputs", exist_ok=True)
    os.makedirs("notebooks", exist_ok=True)

def main():
    ensure_dirs()

    # Step 1: Generate prompt
    prompt = build_prompt(None, "deceptive")
    save_prompt(prompt, "data/prompts/deceptive_prompt.json")

    # Step 2: Run strategies (e.g., deceptive, helpful, vague)
    strategies = ["deceptive", "helpful", "vague"]
    run_strategies(strategies, prompt, output_dir="eval_outputs")

    # Step 3: Evaluate model responses
    evaluate_responses("eval_outputs")

    print("Pipeline complete. Check eval_outputs and strategy_report.md for results.")

if __name__ == "__main__":
    main()