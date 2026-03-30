def dijkstra(graph, src, dest):
    unvisited = set()
    predecessors = {}
    distances = {}

    for node in graph:
        unvisited.add(node)
        distances[node] = float("inf")

    distances[src] = 0

    while unvisited:

        next_nearest = next_nearest_node(distances, unvisited)
        unvisited.remove(next_nearest)

        if next_nearest == dest:
            return get_path(dest, predecessors)

        for neighbor, weight in graph[next_nearest].items():
            if neighbor in unvisited:
                current_dist = distances[next_nearest]
                new_dist = current_dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    predecessors[neighbor] = next_nearest

    return None
      



# Don't touch below this line


def get_path(dest, predecessors):
    path = []
    pred = dest

    while pred is not None:
        path.append(pred)
        pred = predecessors.get(pred, None)

    path.reverse()
    return path


def next_nearest_node(distances, unvisited):
    min_dist = float("inf")
    next_nearest = None

    for v in unvisited:
        distance_so_far = distances[v]
        if distance_so_far < min_dist:
            min_dist = distance_so_far
            next_nearest = v

    return next_nearest
