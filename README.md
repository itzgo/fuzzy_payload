# FuzzML
FuzzML is a lightweight fuzzing engine for machine learning models.
It generates statistically realistic synthetic inputs based on real CSV datasets to stress-test models and preprocessing pipelines.

## Requirements
Python 3.9+
Virtualenv (recommended)

## Installation
git clone https://github.com/itzgo/fuzzy_payload.git
cd fuzzml
python -m venv venv
source venv/bin/activate
pip install pandas numpy
Edit config.py and update the CSV_PATH to point to your dataset.

## Generate fuzz data
python src/runner.py
This will generate a JSON file containing synthetic fuzz payloads:
src/out/fuzz_payloads.json