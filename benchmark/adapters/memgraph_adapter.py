from gqlalchemy import Memgraph
from dotenv import load_dotenv
import os

from benchmark.core.database_interface import DatabaseInterface

load_dotenv()


class MemgraphAdapter(DatabaseInterface):

    def __init__(self):
        self.db = Memgraph(
            host="18.196.41.93",
            port=7687,
            username=os.getenv("MEMGRAPH_USER"),
            password=os.getenv("MEMGRAPH_PASSWORD"),
            encrypted=True,
        )

    def connect(self):
        return self.db

    def test_connection(self):
        self.db.execute("RETURN 1")
        print("✅ Memgraph connected successfully!")

    def create_nodes(self, count):
        pass

    def point_lookup(self):
        self.db.execute(
            """
            MATCH (u:User {id:1})
            RETURN u
            """
        )

    def aggregation_query(self):
        self.db.execute(
            """
            MATCH (u:User)
            RETURN count(u)
            """
        )

    def hop1_query(self):
        self.db.execute(
            """
            MATCH (u:User {id:1})-[:FRIEND]->(n)
            RETURN n
            LIMIT 100
            """
        )

    def hop2_query(self):
        self.db.execute(
            """
            MATCH (u:User {id:1})-[:FRIEND]->()-[:FRIEND]->(n)
            RETURN n
            LIMIT 100
            """
        )

    def hop3_query(self):
        self.db.execute(
            """
            MATCH (u:User {id:1})-[:FRIEND]->()-[:FRIEND]->()-[:FRIEND]->(n)
            RETURN n
            LIMIT 100
            """
        )

    def update_nodes(self):
        self.db.execute(
            """
            MATCH (n:User)
            WITH n LIMIT 100
            SET n.updated = true
            """
        )

    def shortest_path(self):
        self.db.execute(
            """
            MATCH (a:User {id:1})-[*..3]-(b:User {id:100})
            RETURN a,b
            LIMIT 1
            """
        )

    def close(self):
        pass


if __name__ == "__main__":
    db = MemgraphAdapter()
    db.test_connection()