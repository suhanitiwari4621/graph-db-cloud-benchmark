from falkordb import FalkorDB
from dotenv import load_dotenv
import os

from benchmark.core.database_interface import DatabaseInterface

load_dotenv()


class FalkorDBAdapter(DatabaseInterface):

    def __init__(self):
        self.db = FalkorDB(
            host=os.getenv("FALKORDB_HOST"),
            port=int(os.getenv("FALKORDB_PORT")),
            username=os.getenv("FALKORDB_USERNAME"),
            password=os.getenv("FALKORDB_PASSWORD"),
        )

    def connect(self):
        return self.db

    def test_connection(self):
        try:
            graph = self.db.select_graph("benchmark")
            graph.query("RETURN 1")
            print("✅ FalkorDB connected successfully!")
        except Exception as e:
            print(f"❌ FalkorDB connection failed: {e}")

    def create_nodes(self, count):
        pass

    def point_lookup(self):
        graph = self.db.select_graph("benchmark")

        graph.query(
            """
            MATCH (u:User {id:1})
            RETURN u
            """
        )

    def aggregation_query(self):
        graph = self.db.select_graph("benchmark")

        graph.query(
            """
            MATCH (u:User)
            RETURN count(u)
            """
        )

    def hop1_query(self):
        graph = self.db.select_graph("benchmark")

        graph.query(
            """
            MATCH (u:User {id:1})-[:FRIEND]->(n)
            RETURN n
            LIMIT 100
            """
        )

    def hop2_query(self):
        graph = self.db.select_graph("benchmark")

        graph.query(
            """
            MATCH (u:User {id:1})-[:FRIEND]->()-[:FRIEND]->(n)
            RETURN n
            LIMIT 100
            """
        )

    def hop3_query(self):
        graph = self.db.select_graph("benchmark")

        graph.query(
            """
            MATCH (u:User {id:1})-[:FRIEND]->()-[:FRIEND]->()-[:FRIEND]->(n)
            RETURN n
            LIMIT 100
            """
        )

    def update_nodes(self):
        graph = self.db.select_graph("benchmark")

        graph.query(
            """
            MATCH (n:User)
            WITH n LIMIT 100
            SET n.updated = true
            """
        )

    def shortest_path(self):
        graph = self.db.select_graph("benchmark")

        graph.query(
            """
            MATCH (a:User {id:1})-[*..3]-(b:User {id:100})
            RETURN a,b
            LIMIT 1
            """
        )

    def close(self):
        pass


if __name__ == "__main__":
    db = FalkorDBAdapter()
    db.test_connection()