import pandas as pd

df = pd.read_csv("data/graph_dataset.csv")

nodes = pd.concat([df["source"], df["target"]]).drop_duplicates()

pd.DataFrame({"id": nodes}).to_csv("User.csv", index=False)

df[["source", "target"]].to_csv("FRIEND.csv", index=False)

print("Done")