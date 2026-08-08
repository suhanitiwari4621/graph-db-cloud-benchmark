import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Database": ["Neo4j", "Memgraph", "FalkorDB", "ArangoDB", "CognoDB"],
    "Point Lookup": [0.300, 3.990, 0.612, 2.137, 0.376],
    "Aggregation": [0.300, 1.853, 0.059, 0.716, 0.448],
    "1-Hop": [0.303, 1.021, 0.675, 0.410, 0.606],
    "2-Hop": [0.315, 1.529, 0.600, 0.718, 0.530],
    "3-Hop": [0.214, 1.638, 0.920, 0.520, 0.603],
    "Update": [0.379, 1.288, 0.205, 0.336, 0.512],
    "Shortest Path": [0.218, 1.169, 0.523, 0.788, 1.426],
}

df = pd.DataFrame(data)

# Point Lookup
plt.figure(figsize=(8,5))
plt.bar(df["Database"], df["Point Lookup"])
plt.title("Point Lookup Latency")
plt.ylabel("Seconds")
plt.tight_layout()
plt.savefig("point_lookup.png")
plt.close()

# Traversal
plt.figure(figsize=(10,5))
x = range(len(df))

plt.bar(x, df["1-Hop"], width=0.25, label="1-Hop")
plt.bar([i + 0.25 for i in x], df["2-Hop"], width=0.25, label="2-Hop")
plt.bar([i + 0.50 for i in x], df["3-Hop"], width=0.25, label="3-Hop")

plt.xticks([i + 0.25 for i in x], df["Database"])
plt.ylabel("Seconds")
plt.title("Traversal Latency")
plt.legend()
plt.tight_layout()
plt.savefig("traversal.png")
plt.close()

# Update
plt.figure(figsize=(8,5))
plt.bar(df["Database"], df["Update"])
plt.title("Update Latency")
plt.ylabel("Seconds")
plt.tight_layout()
plt.savefig("update.png")
plt.close()

# Shortest Path
plt.figure(figsize=(8,5))
plt.bar(df["Database"], df["Shortest Path"])
plt.title("Shortest Path Latency")
plt.ylabel("Seconds")
plt.tight_layout()
plt.savefig("shortest_path.png")
plt.close()

print("Charts generated successfully.")