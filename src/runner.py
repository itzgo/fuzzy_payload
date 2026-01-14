import json
from csv_profile import build_profile
from fuzz_generator import generate_payload
from config import OUTPUT_PATH, FUZZ_RUNS

def run():
    profile = build_profile()
    results = []

    for _ in range(FUZZ_RUNS):
        results.append(generate_payload(profile))

    with open(OUTPUT_PATH, "w") as f:
        json.dump(results, f, indent=2)

    print(f"Generated {FUZZ_RUNS} fuzz payloads → {OUTPUT_PATH}")

if __name__ == "__main__":
    run()

