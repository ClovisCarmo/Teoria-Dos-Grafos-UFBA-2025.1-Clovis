class Graph:
    def __init__(self):
        self.adj_list = {}
        self.edge_labels = {}  # edge weights/labels, keys are frozenset({u,v})

    def add_vertex(self, v):
        if v not in self.adj_list:
            self.adj_list[v] = set()

    def add_edge(self, u, v, label=None):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj_list[u].add(v)
        self.adj_list[v].add(u)
        self.edge_labels[frozenset((u, v))] = label

    def nodes(self):
      return list(self.adj_list.keys())



    def neighbors(self, v):
        return self.adj_list.get(v, set())

    def min_degree(self):
        if not self.adj_list:
            return 0
        return min(len(neigh) for neigh in self.adj_list.values())

    def empty_copy(self):
        new_g = Graph()
        for v in self.adj_list:
            new_g.add_vertex(v)
        return new_g

    def copy(self):
        new_g = self.empty_copy()
        for u in self.adj_list:
            for v in self.adj_list[u]:
                edge = frozenset((u, v))
                if edge not in new_g.edge_labels:
                    new_g.add_edge(u, v, self.edge_labels.get(edge))
        return new_g

    def edge_iterator(self, labels=True):
        seen = set()
        for u in self.adj_list:
            for v in self.adj_list[u]:
                edge = frozenset((u, v))
                if edge not in seen:
                    seen.add(edge)
                    if labels:
                        yield (u, v, self.edge_labels.get(edge))
                    else:
                        yield (u, v)

    def order(self):
        return len(self.adj_list)

    def size(self):
        return sum(len(n) for n in self.adj_list.values())//2

    def delete_edge(self, u, v):
        if v in self.adj_list.get(u, set()):
            self.adj_list[u].remove(v)
        if u in self.adj_list.get(v, set()):
            self.adj_list[v].remove(u)
        self.edge_labels.pop(frozenset((u, v)), None)

    def order_by_weight(self, labels=True):
        edges = list(self.edge_iterator(labels=True))
        edges.sort(key=lambda e: e[2] if e[2] is not None else 1)
        if labels:
            return edges
        else:
            return [(u, v) for u, v, _ in edges]

    def edges(self, sort=False, labels=False):
        edges = list(self.edge_iterator(labels=labels))
        if sort and labels:
            edges.sort(key=lambda e: e[2] if e[2] is not None else 1)
        elif sort and not labels:
            edges.sort(key=lambda e: (e[0], e[1]))
        return edges

    def set_edge_label(self, u, v, label):
        self.edge_labels[frozenset((u, v))] = label

    def edge_label(self, u, v):
        return self.edge_labels.get(frozenset((u, v)))
