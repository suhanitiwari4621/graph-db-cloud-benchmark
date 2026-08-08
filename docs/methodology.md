# Benchmark Methodology

## Objective

The objective of this benchmark is to compare the performance of multiple cloud-hosted graph databases using a common dataset and a standardized set of graph workloads.

## Databases Evaluated

- Neo4j Aura
- Memgraph Cloud
- FalkorDB Cloud
- ArangoDB Cloud
- CognoDB

---

## Dataset

Source:

`soc-pokec-relationships.csv`

Dataset Statistics:

- Nodes: 49,683
- Edges: 100,000

The dataset represents a social network graph where users are connected through friendship relationships.

---

## Benchmark Workloads

### 1. Point Lookup

Retrieve a single user node by its ID.

Purpose:

Measure indexed node retrieval performance.

### 2. Aggregation Query

Count user nodes stored in the graph.

Purpose:

Measure aggregation and graph scanning performance.

### 3. Hop-1 Traversal

Retrieve immediate neighbors of a user node.

Purpose:

Measure single-hop graph traversal efficiency.

### 4. Hop-2 Traversal

Retrieve nodes two hops away from a user node.

Purpose:

Measure medium-depth graph traversal performance.

### 5. Hop-3 Traversal

Retrieve nodes three hops away from a user node.

Purpose:

Measure deeper graph traversal performance.

### 6. Update Operation

Update properties on a subset of user nodes.

Purpose:

Measure write and update performance.

### 7. Shortest Path Query

Compute a path between two user nodes.

Purpose:

Measure graph path-finding performance.

---

## Measurement Procedure

Execution time was measured using Python's high-resolution timer:

```python
time.perf_counter()
```

Each workload was executed independently against every database.

The elapsed execution time was recorded in seconds.

Lower execution time indicates better performance.

---

## Environment

### Software

- Python 3.11
- Official Python database drivers
- Matplotlib (chart generation)

### Cloud Databases

- Neo4j Aura
- Memgraph Cloud
- FalkorDB Cloud
- ArangoDB Cloud
- CognoDB

### Dataset Size

- 49,683 Nodes
- 100,000 Relationships

---

## Benchmark Metric

The benchmark reports:

- Query Execution Time (seconds)

Measured workloads:

- Point Lookup
- Aggregation Query
- Hop-1 Traversal
- Hop-2 Traversal
- Hop-3 Traversal
- Update Operation
- Shortest Path Query

All databases were tested using the same dataset and equivalent graph operations to ensure a fair comparison.