# Graph DB Cloud Benchmark

## Overview

This project benchmarks the performance of multiple cloud-hosted graph databases using a real-world social network dataset.

The benchmark evaluates common graph operations and compares execution times across different graph database platforms.

## Databases Tested

- Neo4j Aura
- Memgraph Cloud
- FalkorDB Cloud
- ArangoDB Cloud
- CognoDB

---

## Dataset

Dataset: `soc-pokec-relationships.csv`

Dataset Statistics:

- Nodes: 49,683
- Edges: 100,000

The dataset represents social network relationships and was used to evaluate graph traversal and update performance.

---

## Project Structure

```text
benchmark/
├── adapters/
│   ├── neo4j_adapter.py
│   ├── memgraph_adapter.py
│   ├── falkordb_adapter.py
│   ├── arangodb_adapter.py
│   └── cognodb_adapter.py
│
├── core/
│   ├── benchmark_runner.py
│   └── database_interface.py
│
├── metrics/
│   └── metrics.py
│
├── workloads/
│   ├── graph_workload.py
│   └── load_data.py
│
├── charts/
├── docs/
├── results/
└── README.md
```

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and configure credentials for all databases.

---

## Load Dataset

```bash
python -m benchmark.workloads.load_data
```

---

## Run Benchmark

```bash
python -m benchmark.core.benchmark_runner
```

---

## Benchmark Workloads

The benchmark executes the following graph workloads:

### 1. Point Lookup

Retrieve a single user node by ID.

### 2. Aggregation Query

Count user nodes in the graph.

### 3. Hop-1 Traversal

Retrieve immediate neighbors of a user node.

### 4. Hop-2 Traversal

Retrieve nodes two hops away.

### 5. Hop-3 Traversal

Retrieve nodes three hops away.

### 6. Update Operation

Update properties on a subset of nodes.

### 7. Shortest Path Query

Compute a path between two user nodes.

---

## Benchmark Results

| Database | Point Lookup | Aggregation | Hop-1 | Hop-2 | Hop-3 | Update | Shortest Path |
|-----------|-------------|-------------|--------|--------|--------|--------|--------------|
| Neo4j | 0.300 | 0.300 | 0.303 | 0.315 | 0.214 | 0.379 | 0.218 |
| Memgraph | 3.990 | 1.853 | 1.021 | 1.529 | 1.638 | 1.288 | 1.169 |
| FalkorDB | 0.612 | 0.059 | 0.675 | 0.600 | 0.920 | 0.205 | 0.523 |
| ArangoDB | 2.137 | 0.716 | 0.410 | 0.718 | 0.520 | 0.336 | 0.788 |
| CognoDB | 0.376 | 0.448 | 0.606 | 0.530 | 0.603 | 0.512 | 1.426 |

---

## Charts

Performance charts are automatically generated using Matplotlib and saved in the `charts/` directory.

Generated charts:

- point_lookup.png
- aggregation_query.png
- hop1_query.png
- hop2_query.png
- hop3_query.png
- update_nodes.png
- shortest_path.png

---

## Key Findings

- Neo4j delivered the strongest overall performance across most workloads.
- FalkorDB achieved the fastest aggregation and update operations.
- ArangoDB performed competitively on graph traversal workloads.
- CognoDB completed all benchmark workloads successfully with stable execution.
- Memgraph successfully executed all workloads but showed higher latency in this benchmark environment.

---

## Conclusion

This benchmark demonstrates the performance characteristics of modern cloud-hosted graph databases under a common workload suite.

Among the tested systems, Neo4j provided the best overall performance, while FalkorDB and ArangoDB showed strong results in specific workload categories.