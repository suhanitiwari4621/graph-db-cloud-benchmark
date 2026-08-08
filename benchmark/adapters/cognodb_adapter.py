from neo4j import GraphDatabase
from dotenv import load_dotenv
import os

from benchmark.core.database_interface import DatabaseInterface

load_dotenv()


class CognoDBAdapter(DatabaseInterface):

    def __init__(self):
        self.driver = GraphDatabase.driver(
            os.getenv("COGNODB_URI"),
            auth=(
                os.getenv("COGNODB_USERNAME"),
                os.getenv("COGNODB_PASSWORD"),
            ),
        )

        self.driver.verify_connectivity()
        print("✅ Connected to CognoDB")

    def connect(self):
        return self.driver

    def test_connection(self):
        try:
            self.driver.verify_connectivity()
            print("✅ CognoDB connected successfully!")
        except Exception as e:
            print(f"❌ CognoDB connection failed: {e}")

    def create_nodes(self, count):
        pass

    def point_lookup(self):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (u:User {id:1})
                RETURN u
                """
            ).consume()

    def aggregation_query(self):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (u:User)
                RETURN count(u)
                """
            ).consume()

    def hop1_query(self):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (u:User {id:1})-[:FRIEND]->(n)
                RETURN n
                LIMIT 100
                """
            ).consume()

    def hop2_query(self):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (u:User {id:1})-[:FRIEND]->()-[:FRIEND]->(n)
                RETURN n
                LIMIT 100
                """
            ).consume()

    def hop3_query(self):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (u:User {id:1})-[:FRIEND]->()-[:FRIEND]->()-[:FRIEND]->(n)
                RETURN n
                LIMIT 100
                """
            ).consume()

    def update_nodes(self):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (n:User)
                WITH n LIMIT 100
                SET n.updated = true
                """
            ).consume()

    def shortest_path(self):
        with self.driver.session() as session:
            session.run(
                """
                MATCH (a:User {id:1})-[*..3]-(b:User {id:100})
                RETURN a,b
                LIMIT 1
                """
            ).consume()

    def close(self):
        if self.driver:
            self.driver.close()
            print("🔒 CognoDB connection closed.")


if __name__ == "__main__":
    db = CognoDBAdapter()
    db.test_connection()
    db.close()