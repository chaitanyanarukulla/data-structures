"""Testing graph.py."""
import pytest


def test_graph_iinitialize_empty_dict(g):
    """Test initialize an empty pq."""
    assert g._graph == {}


def test_add_node(g):
    """Test it adds note."""
    g.add_node(5)
    assert g._graph[5] == []


def test_add_node_returns_list_of_all_nodes(g):
    """Test if add node return list of all nodes."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(8)
    assert 5 in g.nodes()
    assert 7 in g.nodes()
    assert 8 in g.nodes()
    assert type(g.nodes()) == list



def test_edges_return_list_of_tuples_of_all_edges(g):
    """Test if edges returns list of tuples with pairings of each edge."""
    g.add_node(5)
    g.add_node(7)
    g.edges()
    assert g.edges() == []


def test_add_edges_returns_list_of_edges(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    assert g.edges() == [(5, 7)]


def test_add_two_edges(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_edge(5, 7)
    g.add_edge(7, 9)
    assert g.edges() == [(5, 7), (7, 9)]


def test_add_edges_will_add_mutipule_edges_to_a_node(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(5, 7)
    g.add_edge(5, 9)
    g.add_edge(5, 10)
    assert g.edges() == [(5, 7), (5, 9), (5, 10)]


def test_add_edges_with_one_val_in_graph_add_second_val(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(5, 7)
    g.add_edge(5, 9)
    g.add_edge(5, 15)
    assert g.edges() == [(5, 7), (5, 9), (5, 15)]


def test_add_edges_with_first_val_new_and_second_val_in_graph(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(5, 7)
    g.add_edge(5, 9)
    g.add_edge(15, 5)
    assert (15, 5) in g.edges()
    assert (5, 7) in g.edges()
    assert (5, 9) in g.edges()


def test_add_edges_with_two_new_nodes(g):
    """Test add edges when both nodes are new to graph."""
    g.add_edge(19, 100)
    assert g.edges() == [(19, 100)]


def test_del_node_deletes_the_node_given(g):
    """Test del node delets the node."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.del_node(7)
    assert 7 not in g.nodes()


def test_del_node_deletes_the_node_given(g):
    """Test del node delets the node."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    g.add_node(9)
    g.del_node(7)
    assert 7 not in g.nodes()


def test_del_node_raises_value_error(g):
    """Test del node raises value error if node has been deleted."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.del_node(5)
    g.del_node(7)
    g.del_node(9)
    with pytest.raises(ValueError):
        g.del_node(5)


def test_del_edge_deletes_all_edges(g):
    """Test if del_edges deletes all edges."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    g.del_edge(5, 7)
    assert g.edges() == []


def test_del_edge_raises_value_error_if_too_many_edges_deleted(g):
    """Test if del_edges raises value  error."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    g.del_edge(5, 7)
    with pytest.raises(ValueError):
        g.del_edge(5, 7)


def test_del_edge_raises_value_error_if_values_not_in_dict(g):
    """Test if del_edges raises value error for values not in dict."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    g.del_edge(5, 7)
    with pytest.raises(ValueError):
        g.del_edge(9, 0)


def test_has_node_is_false_on_empty_graph(g):
    """Test false if there are no nodes in graph."""
    assert g.has_node(2) is False


def test_has_node_if_value_in_graph(g):
    """Test false if node does not exist."""
    g.add_node(5)
    assert g.has_node(5) is True


def test_neighbors_return_list_of_nodes_connected_to_input(g):
    """Test neighbor retutns the list of nodes connected input value."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    g.add_node(8)
    g.add_node(9)
    g.add_edge(5, 9)
    g.add_edge(5, 8)
    assert g.neighbors(5) == [7, 9, 8]


def test_neighbors_raises_valueerror_if_node_not_exist(g):
    """Test neighbor raises value error if input not a node."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    g.add_node(8)
    g.add_node(9)
    g.add_edge(5, 9)
    with pytest.raises(ValueError):
        g.neighbors(20)


def test_adjacent_if_two_nodes_have_edge_is_true(g):
    """Test adjacent has  edges returns true when edge exists."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    assert g.adjacent(5, 7) is True


def test_adjacent_when_edge_when_no_edges(g):
    """Test adjacent has no edges returns false."""
    g.add_node(5)
    g.add_node(7)
    assert g.adjacent(5, 7) is False


def test_adjacent_raises_valueerror_if_input_not_node(g):
    """Test adjacent raises value error if node does not exist."""
    g.add_node(5)
    g.add_node(7)
    with pytest.raises(ValueError):
        g.adjacent(9, 0)
