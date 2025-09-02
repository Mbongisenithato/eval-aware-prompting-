def evaluate(strategy):
    # Dummy scoring logic
    score = len(strategy.get("tactics", [])) * 10
    strategy["score"] = score
    return strategy

# Example usage
if __name__ == "__main__":
    sample_strategy = {
        "name": "Decoy Maneuver",
        "tactics": ["misdirection", "false signaling"]
    }
    result = evaluate(sample_strategy)
    print(result)