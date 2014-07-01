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
        return (n1, n2) in self._edges

    def add_edge(self, n1, n2, w1=None):
        if not self.has_edge(n1, n2):
            if n1 not in self._nodes:
                self._nodes.append(n1)
            if n2 not in self._nodes:
                self._nodes.append(n2)
            self._edges[(n1, n2)] = w1

    def delete_edge(self, n1, n2):
        try:
            self._edges.pop((n1, n2))
        except(KeyError):
            raise KeyError

    def delete_node(self, n):
        if n not in self._nodes:
            raise IndexError
        for i in self._nodes:
            if self.has_edge(n, i):
                self.delete_edge(n, i)
            elif self.has_edge(i, n):
                self.delete_edge(i, n)
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
        if not self.has_node(n):
            raise IndexError
        if not n._visited:
            n._visited = True
            df.append(n)
            neighbors = self.has_neighbors(n)
            for i in neighbors:
                self.df_traversal(i, df)

    def bf_traversal(self, n):
        if not self.has_node(n):
            raise IndexError
        bf = [n]
        n._visited = True
        for i in bf:
            for child in self.has_neighbors(i):
                if not child._visited:
                    bf.append(child)
                    child._visited = True
        return bf

    def _Dijkstra(self, start, end):
        if (not self.has_node(start)) or (not self.has_node(end)):
            raise IndexError
        v_nodes = {start: (0, None)}

        base = start
        while base != end:
            neighbors = self.has_neighbors(base)
            first_neighbor = True
            for neighbor in neighbors:
                new_weight = self._edges[base, neighbor] + v_nodes[base][0]
                if (neighbor in v_nodes) and (new_weight > v_nodes[neighbor][0]):
                    print "do nothing"
                else:
                    v_nodes[neighbor] = (new_weight, base)
                if first_neighbor:
                    first_neighbor = False
                    smallest = (v_nodes[neighbor][0], neighbor)
                elif smallest[0] > v_nodes[neighbor][0]:
                    smallest = (v_nodes[neighbor][0], neighbor)
            base = smallest[1]
            print smallest[0]
        path_list = []
        tmp_node = end
        while tmp_node:
            path_list.append(tmp_node)
            tmp_node = v_nodes[tmp_node][1]
        return path_list[::-1]


    def visit_reset(self):
        for i in self._nodes:
            i._visited = False


if __name__ == '__main__':
   # import random
    g = Graph()
    a = g.add_node("a")
    b = g.add_node("b")
    c = g.add_node("c")
    d = g.add_node("d")

    g.add_edge(a, b, 1)
    g.add_edge(b, c, 2)
    g.add_edge(a, c, 8)
    g.add_edge(c, d, 1)

    print g._Dijkstra(a, c)

    # for i in range(10):
    #     a = random.randint(10, 99)
    #     g.add_node(a)


#     for i in range(40):
#         a = random.randint(0, 9)
#         b = random.randint(0, 9)
#         g.add_edge(g._nodes[a], g._nodes[b])



    # for i in g._nodes:
    #     result = "Node " + str(i._data) + ": | "
    #     for x in g.has_neighbors(i):
    #         result += str(x._data) + " | "
    #     print result

    # df = []
    # g.df_traversal(g._nodes[0], df)
    # result = "\nDepth First Search: \n\t"
    # for i in df:
    #     result += str(i._data) + " | "
    # g.visit_reset()

    # print result + "\n"
    # bf = g.bf_traversal(g._nodes[0])
    # result = "\nBreadth First Search: \n\t"
    # for i in bf:
    #     result += str(i._data) + " | "
    # print result + "\n"
    # g.visit_reset()
