from benchmark.metrics.metrics import measure


def run_workload(db):
    results = {}

    results["point_lookup"] = measure(db.point_lookup)
    results["aggregation_query"] = measure(db.aggregation_query)

    results["hop1_query"] = measure(db.hop1_query)
    results["hop2_query"] = measure(db.hop2_query)
    results["hop3_query"] = measure(db.hop3_query)

    results["update_nodes"] = measure(db.update_nodes)
    results["shortest_path"] = measure(db.shortest_path)

    return results