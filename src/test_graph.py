"""Testing graph.py."""
# import pytest


def test_graph_iinitialize_empty_dict(g):
    """Test initialize an empty pq."""
    assert g._graph == {}


def test_add_node(g):
    """Test it adds note."""
    g.add_node(5)
    assert g._graph[5] == []


def test_node_returns_list_of_all_nodes(g):
    """Test if nodes return list of all nodes."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(8)
    assert g.nodes() == [5, 7, 8]


def test_edges_return_list_of_all_nodes_edges(g):
    """Test it adds note."""
    g.add_node(5)
    g.add_node(7)
    g.edges()
    assert g.edges() == []

def test_add_nodel_adds_node(g):
    """Test if add_node add nodes."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(8)
    assert g.nodes() == [5, 7, 8]



def test_add_edges_adds_edges(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    assert g.edges() == [(5, 7)]


def test_add_edges_with_e(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_edge(5, 7)
    g.add_edge(7, 9)
    assert g.edges() == [(5, 7), (7, 9)]

def test_add_edges_will_add_mutipul_edges_to_a_node_(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(5, 7)
    g.add_edge(5, 9)
    g.add_edge(5, 10)
    assert g.edges() == [(5, 7), (5, 9), (5, 10)]
