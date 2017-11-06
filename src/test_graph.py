"""Testing graph.py."""
import pytest


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


def test_del_node_delets_the_node(g):
    """Test del node delets the node."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.del_node(7)
    assert g.nodes() == [5, 9]


def test_del_node_raises_valueerroe(g):
    """Test del node delets the node."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.del_node(5)
    g.del_node(7)
    g.del_node(9)
    with pytest.raises(ValueError):
        g.del_node(5)


def test_del_edge_delets_edges(g):
    """Test if del_edges delets edges."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    g.del_edge(5, 7)
    assert g.edges() == []


def test_del_edge_raises_value_error(g):
    """Test if del_edges raises value  error."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    g.del_edge(5, 7)
    with pytest.raises(ValueError):
        g.del_edge(5, 7)


def test_del_edge_raises_key_error(g):
    """Test if del_edges raises value  error."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    g.del_edge(5, 7)
    with pytest.raises(ValueError):
        g.del_edge(9, 0)


def test_has_node_has_no_node(g):
    """Test false if there is no node."""
    assert g.has_node(2) is False


def test_has_node_has_node(g):
    """Test false if there is no node."""
    g.add_node(5)
    assert g.has_node(5) is True

def test_neighbors_return_list_of_nodes_connected(g):
    """Test neighbor retutns the list of nodes connected."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    g.add_node(8)
    g.add_node(9)
    g.add_edge(5, 9)
    g.add_edge(5, 8)
    assert g.neighbors(5) == [7, 9, 8]


def test_neighbors_raises_valueerror(g):
    """Test neighbor retutns the list of nodes connected."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    g.add_node(8)
    g.add_node(9)
    g.add_edge(5, 9)
    with pytest.raises(ValueError):
        g.neighbors(20)


def test_adjacent_has_any_edges(g):
    """Test adjacent has  edges returns true."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    assert g.adjacent(5, 7) is True


def test_adjacent_has_no_edges(g):
    """Test adjacent has no edges returns false."""
    g.add_node(5)
    g.add_node(7)
    assert g.adjacent(5, 7) is False


def test_adjacent_raises_valueerror(g):
    """Test adjacent has no edges returns false."""
    g.add_node(5)
    g.add_node(7)
    with pytest.raises(ValueError):
        g.adjacent(9, 0)
