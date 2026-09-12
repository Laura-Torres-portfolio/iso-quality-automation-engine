import os
import numpy as np
import pandas as pd
from datetime import datetime


def generate_mock_food_quality_data(filename="raw_factory_logs.csv"):
    np.random.seed(42)
    rows = 100

    # Simulate 100 log entries from a food processing plant
    data = {
        "batch_id": [f"BAT-{1000 + i}" for i in range(rows)],
        "timestamp": pd.date_range(
            start="2026-09-01", periods=rows, freq="h"
        ).astype(str),
        # Critical Control Point: Storage temp should be between 2.0°C and 4.0°C
        "storage_temp_celsius": np.round(np.random.uniform(1.0, 6.0, rows), 2),
        # ISO 9001: Net weight compliance target = 500g (Tolerance: +/- 5g)
        "package_weight_grams": np.round(
            np.random.normal(500, 3.5, rows), 1
        ),
        # ISO 14001: Energy consumption limit = 150 kWh per batch
        "energy_kwh": np.round(np.random.uniform(110, 180, rows), 1),
        # Quality Manager Sign-off (Missing values simulate compliance failure)
        "qa_signoff_operator": np.random.choice(
            ["Op_Alpha", "Op_Beta", "Op_Gamma", None],
            size=rows,
            p=[0.4, 0.35, 0.15, 0.10],
        ),
    }

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"✅ Generated mock data file: '{filename}' with {rows} records.")


if __name__ == "__main__":
    generate_mock_food_quality_data()
