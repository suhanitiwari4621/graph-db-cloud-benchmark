import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {

    "neo4j": {
        "uri": os.getenv("NEO4J_URI"),
        "username": os.getenv("NEO4J_USERNAME"),
        "password": os.getenv("NEO4J_PASSWORD"),
        "database": os.getenv("NEO4J_DATABASE"),
    },

    "cognodb": {
        "uri": os.getenv("COGNODB_URI"),
        "username": os.getenv("COGNODB_USERNAME"),
        "password": os.getenv("COGNODB_PASSWORD"),
    },

    "memgraph": {
        "uri": os.getenv("MEMGRAPH_URI"),
        "username": os.getenv("MEMGRAPH_USERNAME"),
        "password": os.getenv("MEMGRAPH_PASSWORD"),
    },

    "falkordb": {
        "host": os.getenv("FALKORDB_HOST"),
        "port": int(os.getenv("FALKORDB_PORT", 6379)),
        "username": os.getenv("FALKORDB_USERNAME"),
        "password": os.getenv("FALKORDB_PASSWORD"),
    },

    "arangodb": {
        "host": os.getenv("ARANGODB_HOST"),
        "port": int(os.getenv("ARANGODB_PORT", 8529)),
        "username": os.getenv("ARANGODB_USERNAME"),
        "password": os.getenv("ARANGODB_PASSWORD"),
        "database": os.getenv("ARANGODB_DATABASE"),
    },
}