"""Implement a class for a graph data structure."""


class Graph(object):
    """Graph class."""

    def __init__(self):
        """Initialize a graph."""
        self._graph = {}

    def nodes(self):
        """Return a list of all nodes in graph."""
        return self._graph.keys()

    def edges(self):
        """Return a list of edges in graph."""
        edges = []
        for key in self._graph:
            for i in key:
                edges.append((key, i))
        return edges

    def add_node(self, val):
        """Add a node with value of val to graph."""
        self._graph[val]

    def add_edge(self, val1, val2):
        """Add a new edge to graph between val1 & val2 as well as add vals."""
        if val1 in self._graph and val2 in self._graph:
            if val2 not in self._graph[val1]:
                self._graph[val1].append(val2)
            if val1 not in self._graph[val2]:
                self._graph[val2].append(val1)
        if val1 in self._graph and val2 not in self._graph:
            self._graph[val1].append(val2)
            self._graph[val2] = [val1]
        if val2 in self._graph and val1 not in self._graph:
            self._graph[val2].append(val1)
            self._graph[val1] = [val2]
        else:
            self._graph[val1] = [val2]
            self._graph[val2] = [val1]

    def del_node(self, val):
        """Delete node w/val from graph, raises exception if not exist."""
        if self._graph[val]:
            self._graph.remove(val)
            for key in self._graph:
                for i in self._graph:
                    if i == val:
                        i.remove(val)
        raise ValueError('There is no node of that value in the graph.')

    def del_edge(self, val1, val2):
        """Delete edge between val1 & val2 from graph."""
        if self._graph[val1] and self._graph[val2]:
            for edge in self._graph[val1]:
                if edge == val2:
                    edge.remove(val2)
            for edge in self._graph[val2]:
                if edge == val1:
                    edge.remove(val1)
        raise ValueError('These edges do not exist.')

    def has_node(self, val):
        """Return true or false if node has value."""
        if self._graph[val]:
            return True
        else:
            return False

    def neighbors(self, val):
        """Return list of nodes connected node(val)."""
        return self._graph[val]

    def adjacent(self, val1, val2):
        """Return true if edge between vals, else false, & error if no val."""
        if self._graph[val1] and self._graph[val2]:
            for edge in self._graph[val1]:
                if edge == val2:
                    return True
            for edge in self._graph[val2]:
                if edge == val1:
                    return True
            return False
        raise ValueError('These edges do not exist.')
