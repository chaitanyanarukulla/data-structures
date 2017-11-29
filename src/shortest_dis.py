"""Using Dijkstra's algorithm to solve the shortest path."""


def dijkstra(graph, start, end):
    """Dijkysta algorithm to calculate the shortest path."""
    distance = {start: 0}
    parents = {}

    not_visited = list(graph._graph.keys())

    while not_visited:
        min_node = None
        for val in not_visited:
            if val in distance:
                if min_node is None:
                    min_node = val
                elif distance[val] < distance[min_node]:
                    min_node = val
        not_visited.remove(min_node)
        if graph._graph[min_node] == {}:
            return parents
        else:
            for edge in graph._graph[min_node]:
                length = distance[min_node] + graph._graph[min_node][edge]
                if edge not in distance or length < distance[edge]:
                    distance[edge] = length
                    parents[edge] = min_node

    return parents


def shortest_distance(graph, start, end):
    """Utilize dijkstra to find the shortest path."""
    d = dijkstra(graph, start, end)
    if d == {}:
        raise ValueError('This start node has no edges.')
    path = [end]
    while end != start:
        path.insert(0, d[end])
        end = d[end]
    return path