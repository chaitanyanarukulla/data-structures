"""Testing graph.py."""
from graph import Graph

import pytest


def test_graph_iinitialize_empty_dict(g):
    """Test initialize an empty pq."""
    assert g._graph == {}


def test_add_node(g):
    """Test it adds note."""
    g.add_node(5)
    assert g._graph[5] == {}


def test_nodes_returns_list_of_all_nodes(g):
    """Test nodes return list of all nodes."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(8)
    assert 5 in g.nodes()
    assert 7 in g.nodes()
    assert 8 in g.nodes()
    assert type(g.nodes()) == list


def test_edges_return_list_of_tuples_of_all_edge(g):
    """Test if edges returns dict of tuples as edge and weight as value."""
    g.add_node(5)
    g.add_node(7)
    g.edges()
    assert g.edges() == []


def test_add_edges_returns_dict_of_edges_as_tuple_keys(g):
    """Test if edges are added if 2 val are given with default weight."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7)
    assert g.edges() == [(5, 7, 0)]


def test_add_two_edges(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_edge(5, 7)
    g.add_edge(7, 9)
    assert g.edges() == [(5, 7, 0), (7, 9, 0)]


def test_add_edges_will_add_mutipule_edges_to_a_node(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(5, 7)
    g.add_edge(5, 9)
    g.add_edge(5, 10)
    assert g.edges() == [(5, 7, 0), (5, 9, 0), (5, 10, 0)]


def test_add_edges_with_one_val_in_graph_add_second_val(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(5, 7)
    g.add_edge(5, 9)
    g.add_edge(5, 15)
    assert g.edges() == [(5, 7, 0), (5, 9, 0), (5, 15, 0)]


def test_add_edges_with_first_val_new_and_second_val_in_graph(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(5, 7)
    g.add_edge(5, 9)
    g.add_edge(15, 5)
    assert (15, 5, 0) in g.edges()
    assert (5, 7, 0) in g.edges()
    assert (5, 9, 0) in g.edges()


def test_add_edges_with_two_new_nodes(g):
    """Test add edges when both nodes are new to graph."""
    g.add_edge(19, 100)
    assert g.edges() == [(19, 100, 0)]


def test_del_node_deletes_the_node_given(g):
    """Test del node delets the node."""
    g.add_node(5)
    g.add_node(7)
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
    assert sorted(g.neighbors(5)) == [7, 8, 9]


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


def test_depth_first_one_node_many_edges(g):
    """Test depth first traversal returns all paths from one node."""
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
    g.add_node(9)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(5, 8)
    g.add_edge(5, 9)
    assert 5 in g.depth_first_traversal(5)
    assert 9 in g.depth_first_traversal(5)
    assert 6 in g.depth_first_traversal(5)
    assert 7 in g.depth_first_traversal(5)
    assert 8 in g.depth_first_traversal(5)
    assert type(g.depth_first_traversal(5)) == list


def test_depth_first_node_no_edge_return_only_self(g):
    """Test depth first traversal returns start val if no edges."""
    g.add_node(8)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(10, 8)
    assert g.depth_first_traversal(8) == [8]


def test_depth_first_one_edge_per_node(g):
    """Test depth first traversal returns all paths from one node."""
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
    g.add_node(9)
    g.add_edge(5, 6)
    g.add_edge(6, 7)
    g.add_edge(7, 8)
    g.add_edge(8, 9)
    assert g.depth_first_traversal(5) == [5, 6, 7, 8, 9]


def test_df_raises_value_error_node_not_exist(g):
    """Test df traversal raises value error if val not in graph."""
    with pytest.raises(ValueError):
        g.depth_first_traversal('blerg')


def test_depth_first_many_node_many_edges(g):
    """Test depth first traversal returns all paths from one node."""
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
    g.add_node(9)
    g.add_edge(8, 9)
    g.add_edge(8, 5)
    g.add_edge(5, 9)
    g.add_edge(6, 9)
    g.add_edge(7, 8)
    g.add_edge(9, 5)
    g.add_edge(9, 6)
    g.add_edge(9, 8)
    g.add_edge(6, 5)
    g.add_edge(7, 5)
    g.add_edge(6, 8)
    dt = g.depth_first_traversal(8)
    assert dt == [8, 5, 9, 6] or dt == [8, 9, 6, 5] or dt == [8, 9, 5, 6]


def test_breadth_first_one_node_many_edges(g):
    """Test breadth first traversal returns all paths from one node."""
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
    g.add_node(9)
    g.add_edge(5, 6)
    g.add_edge(5, 7)
    g.add_edge(5, 8)
    g.add_edge(5, 9)
    assert 5 in g.breadth_first_traversal(5)
    assert 9 in g.breadth_first_traversal(5)
    assert 6 in g.breadth_first_traversal(5)
    assert 7 in g.breadth_first_traversal(5)
    assert 8 in g.breadth_first_traversal(5)
    assert type(g.breadth_first_traversal(5)) == list


def test_breadth_first_node_no_edge_return_only_self(g):
    """Test breadth first traversal returns start val if no edges."""
    g.add_node(8)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(10, 8)
    assert g.depth_first_traversal(8) == [8]


def test_bf_raises_value_error_node_not_exist(g):
    """Test bf traversal raises value error if val not in graph."""
    with pytest.raises(ValueError):
        g.depth_first_traversal('blerg')


def test_bf_first_many_node_many_edges(g):
    """Test bf first traversal returns all paths from one node."""
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
    g.add_node(9)
    g.add_edge(5, 9)
    g.add_edge(6, 9)
    g.add_edge(7, 8)
    g.add_edge(8, 5)
    g.add_edge(9, 5)
    g.add_edge(9, 6)
    g.add_edge(9, 8)
    g.add_edge(6, 5)
    g.add_edge(7, 5)
    g.add_edge(8, 9)
    g.add_edge(6, 8)
    assert 5 in g.depth_first_traversal(8)
    assert 9 in g.depth_first_traversal(8)
    assert 6 in g.depth_first_traversal(8)
    assert 5 in g.depth_first_traversal(8)
    # assert g.depth_first_traversal(8) == [8, 9, 6, 5]


def test_breadth_first_works_on_cyclic_graph(g):
    """Test breadth first traversal returns all paths from one node."""
    g.add_node(5)
    g.add_node(6)
    g.add_edge(5, 6)
    g.add_edge(6, 5)
    assert g.breadth_first_traversal(5) == [5, 6]


def test_depth_first_works_on_cyclic_graph(g):
    """Test breadth first traversal returns all paths from one node."""
    g.add_node(5)
    g.add_node(6)
    g.add_edge(5, 6)
    g.add_edge(6, 5)
    assert g.breadth_first_traversal(5) == [5, 6]


def test_add_edges_w_weights_returns_dict_of_edges_as_tuple_keys(g):
    """Test if edges are added if 2 val are given with default weight."""
    g.add_node(5)
    g.add_node(7)
    g.add_edge(5, 7, 6)
    assert g.edges() == [(5, 7, 6)]


def test_add_two_edges_w_weights_(g):
    """Test if edges are added if 2 val are given with weights returns dict."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_edge(5, 7, 100)
    g.add_edge(7, 9, 1)
    assert g.edges() == [(5, 7, 100), (7, 9, 1)]


def test_add_edges_w_weights_will_add_mutipule_edges_to_a_node(g):
    """Test if edges are added if 2 val are given with weights."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(5, 7, 4)
    g.add_edge(5, 9)
    g.add_edge(5, 10, 12039)
    assert g.edges() == [(5, 7, 4), (5, 9, 0), (5, 10, 12039)]


def test_add_edges_with_weights_with_one_val_in_graph_add_second_val(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(5, 7, 0)
    g.add_edge(5, 9, 3)
    g.add_edge(5, 15, 6)
    assert g.edges() == [(5, 7, 0), (5, 9, 3), (5, 15, 6)]


def test_add_edges_w_weights_with_first_val_new_and_second_val_in_graph(g):
    """Test if edges are added if 2 val are given."""
    g.add_node(5)
    g.add_node(7)
    g.add_node(9)
    g.add_node(10)
    g.add_edge(5, 7, 4)
    g.add_edge(5, 9, 7)
    g.add_edge(15, 5, 9)
    assert (15, 5, 9) in g.edges()
    assert (5, 7, 4) in g.edges()
    assert (5, 9, 7) in g.edges()


def test_add_edges_with_weights_with_two_new_nodes(g):
    """Test add edges when both nodes are new to graph."""
    g.add_edge(19, 100, 1000)
    assert g.edges() == [(19, 100, 1000)]


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


def test_dijkstra_returns_best_parents():
    """Test dijkstra returns each nodes best parents."""
    g = Graph()
    g._graph = test_graph
    assert g.dijkstra('A') == {'B': 'A', 'C': 'A', 'D':
                               'B', 'E': 'D', 'F': 'C', 'G': 'D'}


def test_dijkstra_returns_best_parents_on_diffrent_path():
    """Test dijkstra returns each nodes best parents."""
    g = Graph()
    g._graph = test_graph
    assert g.dijkstra('A') == {'B': 'A', 'C': 'A', 'D': 'B', 'E':
                               'D', 'F': 'C', 'G': 'D'}


def test_dijkstra_returns_best_parents_of_the_node():
    """Test dijkstra returns each nodes best parents."""
    g = Graph()
    g._graph = graph
    assert g.dijkstra('A') == {'B': 'A', 'C': 'A', 'D': 'A',
                               'E': 'B', 'F': 'D', 'G': 'D'}


def test_shortest_distance():
    """Test for Shortest path from start node to end node."""
    g = Graph()
    g._graph = graph
    assert g.shortest_distance('A', 'F') == ['A', 'D', 'F']


def test_shortest_distance_returns_list():
    """Test for Shortest path from start node to end node."""
    g = Graph()
    g._graph = test_graph
    assert g.shortest_distance('A', 'E') == ['A', 'B', 'D', 'E']


def test_shortest_distance_returns_list_from_path_a_g():
    """Test for Shortest path from start node to end node."""
    g = Graph()
    g._graph = test_graph
    assert g.shortest_distance('A', 'G') == ['A', 'B', 'D', 'G']


def test_dijkstra_that_start_no_children_return_emty_dict():
    """Test dijkstra returns each nodes best parents."""
    g = Graph()
    g._graph = graph
    assert g.dijkstra('G') == {}


def test_shortest_distance_raises_valueerror_if_start_has_no_edges():
    """Test shortest distance raises ValueError if start has no edges."""
    g = Graph()
    g._graph = test_graph
    with pytest.raises(ValueError):
        g.shortest_distance('G', 'A')
