"""Implement a class for a graph data structure."""


class Graph(object):
    """Graph class."""

    def __init__(self):
        """Initialize a graph."""
        self._graph = {}

    def nodes(self):
        """Return a list of all nodes in graph."""
        return list(self._graph.keys())

    def edges(self):
        """Return a list of edges in graph."""
        edges = []
        for key in self._graph:
            for i in self._graph[key]:
                edges.append((key, i))
        return edges

    def add_node(self, val):
        """Add a node with value of val to graph."""
        self._graph[val] = []

    def add_edge(self, val1, val2):
        """Add a new edge to graph between val1 & val2 as well as add vals."""
        if val1 in self._graph and val2 in self._graph:
            if val2 not in self._graph[val1]:
                self._graph[val1].append(val2)
        elif val1 in self._graph and val2 not in self._graph:
            self._graph[val2] = []
            self._graph[val1].append(val2)
        elif val2 in self._graph and val1 not in self._graph:
            self._graph[val1] = []
            self._graph[val1].append(val2)
        else:
            self._graph[val1] = [val2]
            self._graph[val2] = []

    def del_node(self, val):
        """Delete node w/val from graph, raises exception if not exist."""
        if val in self._graph:
            del self._graph[val]
            for key in self._graph:
                for i in self._graph[key]:
                    if i == val:
                        self._graph[key].remove(val)
        else:
            raise ValueError('There is no node of that value in the graph.')

    def del_edge(self, val1, val2):
        """Delete edge between val1 & val2 from graph."""
        try:
            if val2 in self._graph[val1]:
                self._graph[val1].remove(val2)
            else:
                raise ValueError('These edges do not exist.')
        except KeyError:
            raise ValueError('These edges do not exist.')

    def has_node(self, val):
        """Return true or false if node has value."""
        if val in self._graph:
            return True
        else:
            return False

    def neighbors(self, val):
        """Return list of nodes connected node(val)."""
        try:
            neighbors = self._graph[val]
            for key in self._graph:
                if val in self._graph[key]:
                    if self._graph[key] not in neighbors:
                        neighbors.append(self._graph[key])
            return neighbors
        except KeyError:
            raise ValueError('This node dosent exit')

    def adjacent(self, val1, val2):
        """Return true if edge between vals, else false, & error if no val."""
        if val1 in self._graph or val2 in self._graph:
            if val1 in self._graph[val2]:
                return True
            if val2 in self._graph[val1]:
                return True
            return False
        else:
            raise ValueError('These edges do not exist.')

    def depth_first_traversal(self, start_val):
        """Traverse the graph from first edge of each node until ultimate."""
        if start_val in self._graph:
            depth_traversal = []
            path = [start_val]
            while path:
                val = path.pop()
                if val not in depth_traversal:
                    depth_traversal.append(val)
                    path = path + self._graph[val]
            return depth_traversal
        else:
            raise ValueError('Value is not in graph.')

    def breadth_first_traversal(self, start_val):
        """Traverse the graph by node's edges before moving to next node."""
        if start_val in self._graph:
            depth_traversal = []
            path = [start_val]
            while path:
                val = path.pop(0)
                if val not in depth_traversal:
                    depth_traversal.append(val)
                    path = path + self._graph[val]
            return depth_traversal
        else:
            raise ValueError('Value is not in graph.')


if __name__ == '__main__':
    graph_data = {
        'A': ['B', 'D'],
        'B': ['A', 'E', 'D'],
        'C': ['A', 'B'],
        'D': [],
        'E': ['D', 'C', 'B', 'A']
    }
    g = Graph()
    g._graph = graph_data
    print('Using the following graph:\n\n{}\n\nthe lists below show a '
          'depth_first_traversal followed by a '
          'breadth_first_traversal:'.format(graph_data))
    print('\nDepth First Traversal:')
    print(g.depth_first_traversal('A'))
    print('\nBreadth First Traversal:')
    print(g.breadth_first_traversal('A'))

    graph_data = {
        'George': ['Steve', 'Jane', 'Phil'],
        'Anne': ['Abe', 'Uma', 'George'],
        'George': ['Abe', 'Steve'],
        'Steve': ['Anne'],
        'Abe': ['George', 'Uma', 'Steve', 'Phil'],
        'Uma': ['Steve'],
        'Phil': ['Uma', 'George', 'Phil'],
        'Jane': ['Anne'],
    }
    g2 = Graph()
    g2._graph = graph_data
    print('\n\nHere is another example on the following graph:\n\n{}\n\nthe '
          'lists below, again, show a depth_first_traversal followed by a '
          'breadth_first_traversal:'.format(graph_data))
    print('\nDepth First Traversal:')
    print(g2.depth_first_traversal('Abe'))
    print('\nBreadth First Traversal:')
    print(g2.breadth_first_traversal('Abe'))
