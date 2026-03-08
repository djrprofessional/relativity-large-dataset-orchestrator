import pandas as pd
import yaml

def load_settings(path='config/job_settings.yml'):
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def validate_manifest(csv_path: str, settings_path='config/job_settings.yml'):
    settings = load_settings(settings_path)
    df = pd.read_csv(csv_path)
    missing_cols = [c for c in settings['required_columns'] if c not in df.columns]
    issues = []
    if missing_cols:
        issues.append({'severity': 'error', 'issue': f'Missing required columns: {missing_cols}'})
    if df['control_number'].duplicated().any():
        issues.append({'severity': 'error', 'issue': 'Duplicate control numbers detected'})
    large_file_threshold = settings['large_file_threshold_mb']
    oversized = df[df['file_size_mb'] > large_file_threshold]
    for _, row in oversized.iterrows():
        issues.append({'severity': 'warning', 'issue': f"Large file detected: {row['control_number']} ({row['file_size_mb']} MB)"})
    return df, issues

def plan_batches(df: pd.DataFrame, batch_size: int):
    batches = []
    for start in range(0, len(df), batch_size):
        chunk = df.iloc[start:start+batch_size].copy()
        chunk['batch_id'] = f'BATCH-{len(batches)+1:03d}'
        batches.append(chunk)
    return batches
