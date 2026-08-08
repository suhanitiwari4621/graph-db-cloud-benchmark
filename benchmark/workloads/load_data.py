import time
import pandas as pd
from neo4j.exceptions import SessionExpired, ServiceUnavailable

from benchmark.adapters.neo4j_adapter import Neo4jAdapter
from benchmark.adapters.cognodb_adapter import CognoDBAdapter
from benchmark.adapters.falkordb_adapter import FalkorDBAdapter
from benchmark.adapters.memgraph_adapter import MemgraphAdapter
from benchmark.adapters.arangodb_adapter import ArangoDBAdapter

DATASET = "data/graph_dataset.csv"


def load_edges():
    return pd.read_csv(DATASET)


# ---------------------- Neo4j ----------------------

def load_neo4j():
    df = load_edges()

    query = """
    UNWIND $rows AS row
    MERGE (a:User {id: row.source})
    MERGE (b:User {id: row.target})
    MERGE (a)-[:FRIEND]->(b)
    """

    BATCH_SIZE = 100
    total = len(df)
    start = 0

    while start < total:

        db = Neo4jAdapter()

        try:
            with db.driver.session() as session:

                while start < total:

                    batch = df.iloc[start:start + BATCH_SIZE]

                    rows = [
                        {
                            "source": int(row["source"]),
                            "target": int(row["target"]),
                        }
                        for _, row in batch.iterrows()
                    ]

                    session.run(query, rows=rows).consume()

                    start += BATCH_SIZE

                    print(f"Neo4j: {min(start, total)}/{total}")

            db.close()

        except (SessionExpired, ServiceUnavailable):
            print(f"\n⚠️ Connection dropped at {start}/{total}")
            print("Reconnecting in 5 seconds...\n")

            db.close()
            time.sleep(5)

        except Exception:
            db.close()
            raise

    print("✅ Neo4j loading completed.")


# ---------------------- CognoDB ----------------------

def load_cognodb():
    from neo4j.exceptions import SessionExpired, ServiceUnavailable
    import time

    df = load_edges()

    query = """
    UNWIND $rows AS row
    MERGE (a:User {id: row.source})
    MERGE (b:User {id: row.target})
    MERGE (a)-[:FRIEND]->(b)
    """

    BATCH_SIZE = 100

    total = len(df)
    start = 0

    while start < total:

        db = CognoDBAdapter()

        try:
            with db.driver.session() as session:

                while start < total:

                    batch = df.iloc[start:start + BATCH_SIZE]

                    rows = [
                        {
                            "source": int(r["source"]),
                            "target": int(r["target"]),
                        }
                        for _, r in batch.iterrows()
                    ]

                    session.run(query, rows=rows).consume()

                    start += BATCH_SIZE

                    print(f"CognoDB: {min(start, total)}/{total}")

            db.close()

        except (SessionExpired, ServiceUnavailable):
            print(f"\n⚠️ CognoDB connection dropped at {start}/{total}")
            print("Reconnecting in 5 seconds...\n")

            db.close()
            time.sleep(5)

        except Exception:
            db.close()
            raise

    print("✅ CognoDB loading completed.")


# ---------------------- FalkorDB ----------------------

from benchmark.adapters.falkordb_adapter import FalkorDBAdapter

def load_falkordb():
    print("Loading FalkorDB...")

    db = FalkorDBAdapter()
    graph = db.db.select_graph("benchmark")

    df = load_edges()

    # Create index once
    try:
        graph.query("CREATE INDEX FOR (u:User) ON (u.id)")
    except:
        pass

    # -----------------------------
    # Load all users first
    # -----------------------------
    users = set(df["source"].astype(int)).union(
        set(df["target"].astype(int))
    )

    print(f"Users: {len(users)}")

    USER_BATCH = 5000
    user_list = list(users)

    for i in range(0, len(user_list), USER_BATCH):
        batch = user_list[i:i + USER_BATCH]

        query = """
        UNWIND $rows AS row
        MERGE (:User {id: row.id})
        """

        graph.query(
            query,
            {"rows": [{"id": uid} for uid in batch]}
        )

        print(f"Users: {min(i + USER_BATCH, len(user_list))}/{len(user_list)}")

    # -----------------------------
    # Load edges
    # -----------------------------
    EDGE_BATCH = 5000

    for i in range(0, len(df), EDGE_BATCH):

        batch_df = df.iloc[i:i + EDGE_BATCH]

        rows = [
            {
                "source": int(row["source"]),
                "target": int(row["target"]),
            }
            for _, row in batch_df.iterrows()
        ]

        query = """
        UNWIND $rows AS row
        MATCH (a:User {id: row.source})
        MATCH (b:User {id: row.target})
        MERGE (a)-[:FRIEND]->(b)
        """

        graph.query(query, {"rows": rows})

        print(f"Edges: {min(i + EDGE_BATCH, len(df))}/{len(df)}")

    print("✅ FalkorDB loading completed.")

    db.close()


# ---------------------- Memgraph ----------------------

def load_memgraph():
    print("Creating adapter...")
    db = MemgraphAdapter()

    print("Reading CSV...")
    df = load_edges()

    total = len(df)
    BATCH_SIZE = 5000

    print(f"Loaded {total} rows")

    for start in range(0, total, BATCH_SIZE):

        batch = df.iloc[start:start + BATCH_SIZE]

        rows = [
            {
                "source": int(row["source"]),
                "target": int(row["target"]),
            }
            for _, row in batch.iterrows()
        ]

        query = """
        UNWIND $rows AS row

        MERGE (a:User {id: row.source})
        MERGE (b:User {id: row.target})

        MERGE (a)-[:FRIEND]->(b)
        """

        db.db.execute(query, {"rows": rows})

        print(
            f"Memgraph: {min(start + BATCH_SIZE, total)}/{total}"
        )

    print("✅ Memgraph loading completed.")


# ---------------------- ArangoDB ----------------------

def load_arangodb():
    print("Loading ArangoDB...")

    db = ArangoDBAdapter()
    df = load_edges()

    total = len(df)
    print(f"Loaded {total} rows")

    # ----------------------------
    # Create collections / graph
    # ----------------------------

    if not db.db.has_collection("User"):
        db.db.create_collection("User")

    if not db.db.has_graph("benchmark"):
        graph = db.db.create_graph("benchmark")

        graph.create_edge_definition(
            edge_collection="FRIEND",
            from_vertex_collections=["User"],
            to_vertex_collections=["User"],
        )

    users = db.db.collection("User")
    edges = db.db.collection("FRIEND")

    # ----------------------------
    # Prepare users
    # ----------------------------

    print("Preparing users...")

    unique_users = set(df["source"]).union(set(df["target"]))

    user_docs = [
        {
            "_key": str(int(uid)),
            "id": int(uid),
        }
        for uid in unique_users
    ]

    print(f"Unique users: {len(user_docs)}")

    USER_BATCH_SIZE = 5000

    print("Starting user import...")

    for start in range(0, len(user_docs), USER_BATCH_SIZE):

        batch = user_docs[start:start + USER_BATCH_SIZE]

        users.import_bulk(
            batch,
            on_duplicate="ignore",
        )

        print(
            f"Users: {min(start + USER_BATCH_SIZE, len(user_docs))}/{len(user_docs)}"
        )

    # ----------------------------
    # Prepare edges
    # ----------------------------

    print("Preparing edges...")

    edge_docs = [
        {
            "_key": f"{int(row['source'])}_{int(row['target'])}",
            "_from": f"User/{int(row['source'])}",
            "_to": f"User/{int(row['target'])}",
        }
        for _, row in df.iterrows()
    ]

    print(f"Edges: {len(edge_docs)}")

    EDGE_BATCH_SIZE = 5000

    print("Starting edge import...")

    for start in range(0, len(edge_docs), EDGE_BATCH_SIZE):

        batch = edge_docs[start:start + EDGE_BATCH_SIZE]

        edges.import_bulk(
            batch,
            on_duplicate="ignore",
        )

        print(
            f"ArangoDB: {min(start + EDGE_BATCH_SIZE, len(edge_docs))}/{len(edge_docs)}"
        )

    print("✅ ArangoDB loading completed.")

    db.close()

# ---------------------- Main ----------------------

if __name__ == "__main__":

    print("Loading Neo4j...")
    load_neo4j()

    print("Loading CognoDB...")
    load_cognodb()

    print("Loading FalkorDB...")
    load_falkordb()

    print("Loading Memgraph...")
    load_memgraph()

    print("Loading ArangoDB...")
    load_arangodb()

    print("✅ Done.")