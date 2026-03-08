# Relativity Large Dataset Orchestrator

A starter GitHub project for demonstrating how large document populations can be prepared, chunked, validated, and monitored for import into **Relativity workspaces**.

This project is **inspired by the architecture and workflow concepts shown in the `relativitydev/relativity-import-samples` repository**, which documents the Relativity Import Service API, managed import jobs, structured load-file datasets, and job status handling. The Relativity repository explains that the Import Service API supports importing large numbers of documents, images, and Relativity Dynamic Objects into a workspace through managed import jobs built around structured datasets and load files. citeturn1view0

## What this project demonstrates
- ingest manifest validation before import
- chunking oversized datasets into batch jobs
- simulated job creation and status tracking
- exception logging for missing files and bad metadata
- reporting for eDiscovery and litigation support teams

## Why it is portfolio-relevant
The official samples focus on API usage patterns for import jobs and job operations. This project adds an orchestration layer around that concept for **large data set management**, including preflight validation, chunk planning, and operational reporting. The underlying Relativity samples center on managed import jobs and structured data sets described by load files. citeturn1view0

## Tech Stack
- Python
- Click
- Pandas
- YAML

## Quick Start
```bash
pip install -r requirements.txt
python cli.py validate data/sample_manifest.csv
python cli.py chunk data/sample_manifest.csv --batch-size 3
python cli.py simulate-import data/sample_manifest.csv
```

## Notes
This repository is a **safe portfolio demo**. It does not connect to a live Relativity environment by default. Instead, it models the operational layer you would place around real Import Service API calls.
