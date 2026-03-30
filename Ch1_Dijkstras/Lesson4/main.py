def get_path(dest: str, predecessors: dict[str, str]) -> list[str]:
    path = []
    current = dest
    
    while current is not None:
        path.append(current)
        current = predecessors.get(current)

    path.reverse()
    return path
