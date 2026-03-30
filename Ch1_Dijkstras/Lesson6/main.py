def next_nearest_node(distances, unvisited):
    min_dist = float("inf")
    next_nearest = None

    for v in unvisited:
        distance_so_far = distances[v]
        if distance_so_far < min_dist:
            min_dist = distance_so_far
            next_nearest = v

    return next_nearest
