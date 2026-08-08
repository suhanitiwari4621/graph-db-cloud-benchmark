from benchmark.workloads.graph_workload import run_workload

from benchmark.adapters.neo4j_adapter import Neo4jAdapter
from benchmark.adapters.memgraph_adapter import MemgraphAdapter
from benchmark.adapters.falkordb_adapter import FalkorDBAdapter
from benchmark.adapters.arangodb_adapter import ArangoDBAdapter
from benchmark.adapters.cognodb_adapter import CognoDBAdapter


def run_database(name, adapter_class):
    print(f"\n===== {name} =====")

    db = adapter_class()

    try:
        results = run_workload(db)

        for operation, timing in results.items():
            print(f"{operation}: {timing:.6f} sec")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        try:
            db.close()
        except Exception:
            pass


def main():
    databases = [
        ("Neo4j", Neo4jAdapter),
        ("Memgraph", MemgraphAdapter),
        ("FalkorDB", FalkorDBAdapter),
        ("ArangoDB", ArangoDBAdapter),
        ("CognoDB", CognoDBAdapter),
    ]

    for name, adapter in databases:
        run_database(name, adapter)


if __name__ == "__main__":
    main()