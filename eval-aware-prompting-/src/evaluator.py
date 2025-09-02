import os
import json

def evaluate_responses(output_dir):
    report_lines = []
    for filename in os.listdir(output_dir):
        if filename.endswith('_output.json'):
            path = os.path.join(output_dir, filename)
            with open(path, 'r') as f:
                data = json.load(f)
            score = mock_score(data['response'])
            report_lines.append(f"{data['strategy']}: {score:.2f}")

    with open('strategy_report.md', 'w') as f:
        f.write('# Strategy Evaluation Report\n\n')
        f.write('\n'.join(report_lines))
    print('Evaluation complete. Report saved to strategy_report.md.')

def mock_score(response):
    # Placeholder scoring logic
    return len(response) % 10 + 1  # Just a mock score for now
