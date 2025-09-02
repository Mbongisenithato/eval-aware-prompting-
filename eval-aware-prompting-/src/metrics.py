import pandas as pd

def compute_metrics(results):
    df = pd.DataFrame(results)
    success_rate = df["deception_success"].mean()
    risk_distribution = df["risk_level"].value_counts(normalize=True).to_dict()
    return {
        "success_rate": round(success_rate, 2),
        "risk_distribution": risk_distribution
    }