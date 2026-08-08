import pandas as pd
import os

INPUT_FILE = "data/soc-pokec-relationships.txt"
OUTPUT_FILE = "data/graph_dataset.csv"

print("Reading dataset...")

df = pd.read_csv(
    INPUT_FILE,
    sep="\t",
    header=None,
    names=["source", "target"]
)

print(f"Original edges: {len(df):,}")

# Keep first 100,000 edges
df = df.iloc[:100000].copy()

df["relationship"] = "CONNECTED_TO"

df.to_csv(OUTPUT_FILE, index=False)

print(f"Saved {len(df):,} edges to {OUTPUT_FILE}")