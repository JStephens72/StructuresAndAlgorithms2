def relax_edge(total_distances, node_a, node_b, dist_a_b):
    if total_distances[node_a] + dist_a_b < total_distances[node_b]:
        total_distances[node_b] = total_distances[node_a] + dist_a_b
        return True
    return False       
