"""Using Dijkstra's algorithm to solve the shortest path."""
from graph import Graph

from priorityq import Priorityq

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


g = Graph()
g._graph = graph


def dijkstra(graph, start, end):
    """Dijkysta algorithm to calculate the shortest path."""
    distance = {}
    parents = {}
    # q = {}
    q = Priorityq()

    q.insert(start, 0)

    while q:
        
    for val in q:
        distance[val] = q[val]
        if val == end:
            break
        for edge in graph._graph[val]:
            length = distance[val] + graph._graph[val][edge]
            if edge not in q or length < q[edge]:
                q[edge] = length
                parents[edge] = val

    return parents


def shortest_distance(graph, start, end):
    """Utilize dijkstra to find the shortest path."""
    d = dijkstra(graph, start, end)
    path = [start, end]
    while end != start:
        path.insert(1, d[end])
        end = d[end]
    return path
