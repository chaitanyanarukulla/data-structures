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
            if len(neighbors) == 0:
                return None
            else:
                return neighbors
        except KeyError:
            raise ValueError('This node dosent exit')

    def adjacent(self, val1, val2):
        """Return true if edge between vals, else false, & error if no val."""
        if val1 in self._graph or val2 in self._graph:
            if val2 in self._graph[val1]:
                return True
            else:
                return False
        else:
            raise ValueError('These edges do not exist.')
