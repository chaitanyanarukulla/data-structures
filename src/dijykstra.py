"""Using Dijkstra's algorithm to solve the shortest path."""
from graph import Graph


graph = {
    'A': {'C': 4,
          'B': 2,
          'D': 5
          },
    'C': {'G': 20,
          'D': 8
          },
    'B': {'E': 8
          },
    'D': {'C': 4,
          'B': 3,
          'F': 10,
          'G': 15
          },
    'E': {'F': 8,
          'D': 8
          },
    'F': {'G': 5
          },
    'G': {}
}

test_graph = {
    'A': {'B': 5,
          'C': 6
          },
    'B': {'D': 2
          },
    'C': {'E': 8,
          'F': 4
          },
    'D': {'E': 2,
          'G': 10
          },
    'E': {'G': 10,
          'F': 4
          },
}

g = Graph()
g._graph = graph


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
