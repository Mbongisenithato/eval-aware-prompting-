import os
import json
import pandas as pd

def load_outputs(output_dir='eval_outputs'):
    records = []
    for file in os.listdir(output_dir):
        if file.endswith('_output.json'):
            with open(os.path.join(output_dir, file), 'r') as f:
                data = json.load(f)
                records.append(data)
    return pd.DataFrame(records)

df = load_outputs()
print(df.head())
