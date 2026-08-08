# Graph DB Cloud Benchmark

## Overview

This project benchmarks the performance of multiple cloud-hosted graph database platforms using a common social network dataset and standardized graph workloads.

The objective is to compare how different graph databases perform when executing typical graph operations such as lookups, traversals, aggregations, updates, and shortest-path queries under the same conditions.

---

## Databases Evaluated

The following managed graph database platforms were evaluated:

- Neo4j Aura
- Memgraph Cloud
- FalkorDB Cloud
- ArangoDB Cloud
- CognoDB

Each platform was accessed through its official Python driver or client library and benchmarked using a common workload implementation.

---

## Features

- Unified benchmarking framework
- Common workload implementation across databases
- Automated performance measurement
- Cloud database comparison
- Performance visualization using charts
- Reproducible benchmarking methodology

---

## Dataset

This benchmark uses a processed subset of the **Pokec Social Network Dataset**, a widely used graph dataset for social network analysis.

### Dataset Statistics

| Metric | Value |
|----------|----------|
| Nodes | 49,683 |
| Edges | 100,000 |
| Graph Type | Social Network |

The dataset represents user-to-user relationships and provides a realistic graph structure for evaluating traversal and pathfinding operations.

### Dataset Source

The original dataset is publicly available through the Stanford Network Analysis Project (SNAP):

https://snap.stanford.edu/data/soc-Pokec.html

The original dataset is not included in this repository due to its size.

A processed dataset used for benchmarking is included as:

```text
data/graph_dataset.csv
```

---

## Project Structure

```text
graph-db-cloud-benchmark/
│
├── benchmark/
│   ├── adapters/
│   │   ├── neo4j_adapter.py
│   │   ├── memgraph_adapter.py
│   │   ├── falkordb_adapter.py
│   │   ├── arangodb_adapter.py
│   │   └── cognodb_adapter.py
│   │
│   ├── core/
│   │   ├── benchmark_runner.py
│   │   └── database_interface.py
│   │
│   ├── metrics/
│   │   └── metrics.py
│   │
│   └── workloads/
│       ├── graph_workload.py
│       └── load_data.py
│
├── charts/
├── configs/
├── data/
├── docs/
├── results/
│
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/suhanitiwari4621/graph-db-cloud-benchmark.git
cd graph-db-cloud-benchmark
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Configuration

Create a `.env` file in the project root and provide the required database credentials.

Example:

```env
# Neo4j
NEO4J_URI=
NEO4J_USERNAME=
NEO4J_PASSWORD=

# Memgraph
MEMGRAPH_URI=
MEMGRAPH_USERNAME=
MEMGRAPH_PASSWORD=

# FalkorDB
FALKORDB_HOST=
FALKORDB_PORT=
FALKORDB_USERNAME=
FALKORDB_PASSWORD=

# ArangoDB
ARANGO_HOST=
ARANGO_USER=
ARANGO_PASSWORD=

# CognoDB
COGNODB_URI=
COGNODB_USERNAME=
COGNODB_PASSWORD=
```

---

## Loading Data

Load the dataset into the configured graph database:

```bash
python -m benchmark.workloads.load_data
```

---

## Running the Benchmark

Execute all benchmark workloads:

```bash
python -m benchmark.core.benchmark_runner
```

Benchmark results will be displayed in the console and can be stored in the `results/` directory.

---

## Benchmark Workloads

The benchmark executes the following graph operations:

### 1. Point Lookup

Retrieve a single node using its identifier.

### 2. Aggregation Query

Perform aggregate calculations over graph data.

### 3. Hop-1 Traversal

Retrieve immediate neighboring nodes.

### 4. Hop-2 Traversal

Retrieve nodes two relationships away.

### 5. Hop-3 Traversal

Retrieve nodes three relationships away.

### 6. Update Operation

Modify properties on existing nodes.

### 7. Shortest Path Query

Compute the shortest path between two nodes.

---

## Benchmark Results

| Database | Point Lookup | Aggregation | Hop-1 | Hop-2 | Hop-3 | Update | Shortest Path |
|----------|-------------|-------------|--------|--------|--------|--------|---------------|
| Neo4j | 0.300 | 0.300 | 0.303 | 0.315 | 0.214 | 0.379 | 0.218 |
| Memgraph | 3.990 | 1.853 | 1.021 | 1.529 | 1.638 | 1.288 | 1.169 |
| FalkorDB | 0.612 | 0.059 | 0.675 | 0.600 | 0.920 | 0.205 | 0.523 |
| ArangoDB | 2.137 | 0.716 | 0.410 | 0.718 | 0.520 | 0.336 | 0.788 |
| CognoDB | 0.376 | 0.448 | 0.606 | 0.530 | 0.603 | 0.512 | 1.426 |

Detailed benchmark outputs are available in:

```text
results/benchmark_results.md
```

---

## Charts

Performance visualizations are generated using Matplotlib and saved in the `charts/` directory.

Generated charts include:

- point_lookup.png
- aggregation_query.png
- hop1_query.png
- hop2_query.png
- hop3_query.png
- update_nodes.png
- shortest_path.png

To regenerate charts:

```bash
python charts/generate_charts.py
```

---

## Methodology

The benchmark was conducted using the following approach:

- All databases were deployed as managed cloud instances.
- The same dataset was loaded into each database.
- Identical workloads were executed across all platforms.
- Execution time was measured using Python's `time.perf_counter()`.
- Results were recorded in seconds.
- Official database drivers and client libraries were used for all interactions.

A detailed methodology document is available in:

```text
docs/methodology.md
```

---

## Key Findings

- Neo4j delivered the strongest overall performance across most workloads.
- FalkorDB achieved the fastest aggregation and update operations.
- ArangoDB showed competitive traversal performance.
- CognoDB completed all benchmark workloads successfully with stable execution.
- Memgraph executed all workloads successfully but exhibited higher latency in this benchmark environment.

Performance may vary depending on deployment size, cloud region, network latency, and dataset scale.

---

## Conclusion

This project provides a reproducible framework for benchmarking cloud-hosted graph databases using a common dataset and standardized graph workloads.

The results demonstrate that different graph databases excel in different workload categories. While Neo4j showed the strongest overall performance in this benchmark, FalkorDB and ArangoDB performed well in specific operations, highlighting the importance of selecting a database based on workload requirements rather than relying solely on overall performance metrics.

Future work may include larger datasets, concurrent workload testing, additional graph algorithms, and support for more graph database platforms.

---

## License

This project was developed for educational and benchmarking purposes.

The Pokec dataset remains subject to the licensing and usage terms specified by the Stanford SNAP project.
