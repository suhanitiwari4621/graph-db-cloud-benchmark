import os
import urllib3

from dotenv import load_dotenv
from arango import ArangoClient

from benchmark.core.database_interface import DatabaseInterface

load_dotenv()

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class ArangoDBAdapter(DatabaseInterface):

    def __init__(self):
        self.client = ArangoClient(
            hosts=os.getenv("ARANGO_HOST"),
            verify_override=False,
        )

        self.db = self.client.db(
            "_system",
            username=os.getenv("ARANGO_USER"),
            password=os.getenv("ARANGO_PASSWORD"),
        )

    def connect(self):
        return self.db

    def test_connection(self):
        print("ArangoDB Version:", self.db.version())
        print("✅ ArangoDB connected successfully!")

    def create_nodes(self, count):
        pass

    def point_lookup(self):
        self.db.aql.execute(
            """
            RETURN DOCUMENT("User/1")
            """
        )

    def aggregation_query(self):
        self.db.aql.execute(
            """
            FOR u IN User
            COLLECT WITH COUNT INTO length
            RETURN length
            """
        )

    def hop1_query(self):
        self.db.aql.execute(
            """
            FOR v,e IN 1..1 OUTBOUND 'User/1' GRAPH 'benchmark'
            LIMIT 100
            RETURN v
            """
        )

    def hop2_query(self):
        self.db.aql.execute(
            """
            FOR v,e IN 2..2 OUTBOUND 'User/1' GRAPH 'benchmark'
            LIMIT 100
            RETURN v
            """
        )

    def hop3_query(self):
        self.db.aql.execute(
            """
            FOR v,e IN 3..3 OUTBOUND 'User/1' GRAPH 'benchmark'
            LIMIT 100
            RETURN v
            """
        )

    def update_nodes(self):
        self.db.aql.execute(
            """
            FOR u IN User
            LIMIT 100
            UPDATE u WITH {updated:true} IN User
            """
        )

    def shortest_path(self):
        self.db.aql.execute(
            """
            FOR v,e IN 1..3 ANY 'User/1' GRAPH 'benchmark'
            LIMIT 1
            RETURN v
            """
        )

    def close(self):
        pass


if __name__ == "__main__":
    db = ArangoDBAdapter()
    db.test_connection()
    db.close()