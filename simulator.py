import random
import pandas as pd

def simulate_import_jobs(batches: list[pd.DataFrame]):
    jobs = []
    for i, batch in enumerate(batches, start=1):
        jobs.append({
            'job_id': f'JOB-{i:03d}',
            'batch_id': batch['batch_id'].iloc[0],
            'document_count': len(batch),
            'status': random.choice(['Completed', 'Completed', 'CompletedWithWarnings', 'Queued']),
        })
    return pd.DataFrame(jobs)
