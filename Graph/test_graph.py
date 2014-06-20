import pytest
from graph import Node, Graph


@pytest.fixture(scope="function")
def initialize_graph():
    g = Graph()
    a = g.add_node("a")
    b = g.add_node("b")
    c = g.add_node("c")
    return a, b, c, g


def test_node():
    a = Node("a")
    assert a._data == "a"


def test_graph():
    g = Graph()
    assert len(g._edges) == 0
    assert len(g._nodes) == 0


def test_graph_2():
    g = Graph("a", "b", "c")
    assert len(g._edges) == 0
    assert len(g._nodes) == 3


def test_add_node():
    g = Graph()
    a = Node("a")
    g.add_node(a)
    assert len(g._nodes) == 1


def test_has_edge(initialize_graph):
    a, b, c, g = initialize_graph
    assert not g.has_edge(a, b)


def test_add_edge(initialize_graph):
    a, b, c, g = initialize_graph
    g.add_edge(a, b)
    assert (a, b) in g._edges

    g.add_edge(b, a)
    assert (b, a) not in g._edges


def test_has_edges_2(initialize_graph):
    a, b, c, g = initialize_graph
    g.add_edge(a, b)
    assert g.has_edge(b, a)


def test_delete_edge(initialize_graph):
    a, b, c, g = initialize_graph
    g.add_edge(a, b)
    g.delete_edge(a, b)
    assert not g.has_edge(a, b)
    assert not g.has_edge(b, a)


def test_delete_non_edge(initialize_graph):
    a, b, c, g = initialize_graph
    g.add_edge(a, b)
    with pytest.raises(KeyError):
        g.delete_edge(a, c)


def test_delete_node(initialize_graph):
    a, b, c, g = initialize_graph
    g.add_edge(a, b)
    g.add_edge(b, c)

    g.delete_node(b)

    assert b not in g._nodes

    for key in g._edges.iterkeys():
        assert b != key[0] and b != key[1]


def test_delete_nonexistent_node(initialize_graph):
    a, b, c, g = initialize_graph

    d = Node("d")

    with pytest.raises(IndexError):
        g.delete_node(d)


def test_has_node(initialize_graph):
    a, b, c, g = initialize_graph
    assert g.has_node(a)

    d = Node("d")

    assert g.has_node(d) is False


def test_has_neighbors(initialize_graph):
    a, b, c, g = initialize_graph
    g.add_edge(a, b)
    g.add_edge(a, c)

    assert g.has_neighbors(a) == [b, c]


def test_adjacent(initialize_graph):
    a, b, c, g = initialize_graph
    g.add_edge(a, b)
    g.add_edge(a, c)

    d = g.add_node("d")
    e = g.add_node("e")
    g.add_edge(a, d)

    assert g.adjacent(a, c)
    assert g.adjacent(a, e) is False

def test_depth(initialize_graph):
    a, b, c, g = initialize_graph
    d = g.add_node("d")
    g.add_edge(a, b)
    g.add_edge(b, d)
    g.add_edge(a, d)
    g.add_edge(b, c)
    assert g.df_traversal(a) == [a, b, c, d]