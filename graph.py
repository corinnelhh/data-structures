class Node(object):

    def __init__(self, data):
        self._data = data


class Graph(object):

    def __init__(self, *data):
        self._edges = {}
        self._nodes = []
        for node in data:
            self._nodes.append(Node(node))

    def add_node(self, data):
        a = Node(data)
        self._nodes.append(a)
        return a

    def has_edge(self, n1, n2):
        return ((n1, n2) in self._edges) or ((n2, n1) in self._edges)

    def add_edge(self, n1, n2, w=1):
        if not self.has_edge(n1, n2):
            if n1 not in self._nodes:
                self._nodes.append(n1)
            if n2 not in self._nodes:
                self._nodes.append(n2)
            self._edges[(n1, n2)] = w

    #def 


if __name__ == '__main__':
    g = Graph()
    a = g.add_node("a")
    b = g.add_node("b")
    g.add_edge(a, b)
    for key, value in g._edges.iteritems():
        print key[0]._data, key[1]._data, value
