class Node(object):

    def __init__(self, data):
        self._data = data
        self._visited = False


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

    def delete_edge(self, n1, n2):
        try:
            self._edges.pop((n1, n2))
        except(KeyError):
            try:
                self._edges.pop((n2, n1))
            except(KeyError):
                raise KeyError

    def delete_node(self, n):
        if n not in self._nodes:
            raise IndexError
        for i in self._nodes:
            if self.has_edge(n, i):
                self.delete_edge(n, i)
        self._nodes.remove(n)

    def has_node(self, n):
        return n in self._nodes

    def has_neighbors(self, n):
        neighbors = []
        if n not in self._nodes:
            raise IndexError
        for i in self._nodes:
            if self.has_edge(n, i):
                neighbors.append(i)
        return neighbors

    def adjacent(self, n1, n2):
        if not self.has_node(n1) or not self.has_node(n2):
            raise IndexError
        return self.has_edge(n1, n2)

    def df_traversal(self, n, df):
        if not n._visited:
            n._visited = True
            df.append(n)
            neighbors = self.has_neighbors(n)
            for i in neighbors:
                self.df_traversal(i,df)


    def bf_traversal(self, n):
        return [n]


if __name__ == '__main__':
    g = Graph()
    a = g.add_node("a")
    b = g.add_node("b")
    c = g.add_node("c")
    d = g.add_node("d")
    e = g.add_node("e")
    g.add_edge(a, b)
    g.add_edge(a, c)
    g.add_edge(a, d)
    g.add_edge(a, e)
    g.add_edge(b, c)
    g.add_edge(b, d)
    g.add_edge(b, e)
    g.add_edge(c, d)
    g.add_edge(c, e)
    g.add_edge(d, e)

    df = []
    print str(g.df_traversal(d,df))
    for i in df:
        print i._data

