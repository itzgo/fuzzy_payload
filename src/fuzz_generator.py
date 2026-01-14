import random
import numpy as np

def generate_payload(profile):
    payload = {}

    for col, p in profile.items():
        if p["type"] == "numeric":
            val = np.random.normal(p["mean"], p["std"])
            val = max(p["min"], min(p["max"], val))
            payload[col] = round(float(val), 4)

        else:
            payload[col] = random.choice(p["values"])

    return payload
