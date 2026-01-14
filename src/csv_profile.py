import pandas as pd
from config import CSV_PATH, SAMPLE_SIZE

def build_profile():
    # leitura única e rápida
    df = pd.read_csv(CSV_PATH)

    # amostra rápida
    if len(df) > SAMPLE_SIZE:
        df = df.sample(SAMPLE_SIZE)

    profile = {}

    for col in df.columns:
        s = df[col].fillna(0)

        if s.dtype.kind in "iuf":
            profile[col] = {
                "type": "numeric",
                "min": float(s.min()),
                "max": float(s.max()),
                "mean": float(s.mean()),
                "std": float(s.std()) or 1
            }
        else:
            profile[col] = {
                "type": "categorical",
                "values": list(s.astype(str).unique())
            }

    return profile