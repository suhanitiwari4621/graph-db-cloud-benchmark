# Benchmark Results

## Dataset

- Nodes: 49,683
- Edges: 100,000

---

## Performance Results (Seconds)

| Database | Point Lookup | Aggregation | Hop-1 | Hop-2 | Hop-3 | Update | Shortest Path |
|-----------|-------------|-------------|--------|--------|--------|--------|--------------|
| Neo4j | 0.300 | 0.300 | 0.303 | 0.315 | 0.214 | 0.379 | 0.218 |
| Memgraph | 3.990 | 1.853 | 1.021 | 1.529 | 1.638 | 1.288 | 1.169 |
| FalkorDB | 0.612 | 0.059 | 0.675 | 0.600 | 0.920 | 0.205 | 0.523 |
| ArangoDB | 2.137 | 0.716 | 0.410 | 0.718 | 0.520 | 0.336 | 0.788 |
| CognoDB | 0.376 | 0.448 | 0.606 | 0.530 | 0.603 | 0.512 | 1.426 |

---

## Performance Ranking

### Point Lookup

1. Neo4j (0.300 s)
2. CognoDB (0.376 s)
3. FalkorDB (0.612 s)
4. ArangoDB (2.137 s)
5. Memgraph (3.990 s)

### Aggregation Query

1. FalkorDB (0.059 s)
2. Neo4j (0.300 s)
3. CognoDB (0.448 s)
4. ArangoDB (0.716 s)
5. Memgraph (1.853 s)

### Shortest Path

1. Neo4j (0.218 s)
2. FalkorDB (0.523 s)
3. ArangoDB (0.788 s)
4. Memgraph (1.169 s)
5. CognoDB (1.426 s)

---

## Observations

- Neo4j achieved the best overall performance across most workloads.
- FalkorDB delivered the fastest aggregation and update performance.
- ArangoDB performed competitively on traversal operations.
- CognoDB completed all benchmark workloads successfully and showed performance close to Neo4j for several queries.
- Memgraph successfully executed all workloads but exhibited higher latency than the other tested systems.

---

## Summary

The benchmark demonstrates the performance characteristics of five cloud-hosted graph database platforms using a common social-network dataset.

Among the evaluated systems:

- Neo4j provided the strongest overall performance.
- FalkorDB excelled in aggregation and update operations.
- ArangoDB showed balanced traversal performance.
- CognoDB completed all workloads reliably with competitive execution times.
- Memgraph supported all benchmark operations but produced the highest query latencies in this environment.

All measurements were collected using the same dataset and equivalent graph workloads to ensure a fair comparison.