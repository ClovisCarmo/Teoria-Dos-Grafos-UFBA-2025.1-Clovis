def edge_disjoint_spanning_trees(G, k, weights=False):
    print(f"Starting edge_disjoint_spanning_trees with k={k}")
    if k > 1 + G.min_degree() // 2:
        raise ValueError("this graph does not contain the required number of trees/arborescences")

    # Inicializa DisjointSets para manter as partições dos grafos.
    partition = [DisjointSet(G.nodes()) for _ in range(k + 1)]

    # Mapeamento de cada aresta para a floresta na qual ela está contida.
    edge_index = {frozenset(e): 0 for e in G.edge_iterator(labels=False)}

    # Cópia vazia do grafo para construir as florestas.
    G_spanning = G.empty_copy()
    F = [G_spanning.copy() for _ in range(k + 1)]

    if weights:
        edges_ordered = list(G.order_by_weight(labels=True))
        print("Edges ordered (with weights):")
        print(edges_ordered)
        edge_weights = {frozenset((u, v)): w for u, v, w in edges_ordered}
    else:
        edges_ordered = list(G.order_by_weight(labels=False))
        edge_weights = {frozenset((u, v)): None for u, v in edges_ordered}

    for idx, edge in enumerate(edges_ordered, 1):
        if weights:
            x, y, w = edge
        else:
            x, y = edge
            w = None

        # Se os dois vértices já estão unidos em partition[0] (o clump global), ignora a aresta.
        if partition[0].find(x) == partition[0].find(y):
            continue

        edge_label = {}
        queue = [(x, y)]
        queue_begin = 0
        queue_end = 1

        # p[i] armazenará os predecessores (raiz x) na floresta F[i] obtida por BFS.
        p = [{x: x} for _ in range(k + 1)]
        for i in range(1, k + 1):
            for u, v in BFS_edges(F[i], x):
                p[i][v] = u

        augmenting_sequence_found = False

        while queue_begin < queue_end:
            e = queue[queue_begin]
            queue_begin += 1
            fe = frozenset(e)
            # Escolhe a floresta i com base em edge_index (alternando de 1 a k)
            i = (edge_index[fe] % k) + 1
            v, w_ = e

            if partition[i].find(v) != partition[i].find(w_):
                augmenting_sequence_found = True
                break
            else:
                if v == x or (v in p[i] and frozenset((v, p[i][v])) in edge_label):
                    u = w_
                else:
                    u = v
                edges_to_label = []
                while u != x and (u in p[i] and frozenset((u, p[i][u])) not in edge_label):
                    edges_to_label.append((u, p[i][u]))
                    u = p[i][u]

                while edges_to_label:
                    ep = edges_to_label.pop()
                    edge_label[frozenset(ep)] = fe
                    queue.append(ep)
                    queue_end += 1

        if augmenting_sequence_found:
            # Atualiza a partição da floresta i incrementando com a aresta atual
            partition[i].union(v, w_)

            # Loop de augmentação: troca arestas entre florestas de forma incremental
            while fe in edge_label:
                old_forest = edge_index[fe]
                u, vv = tuple(fe)
                # Remove aresta da floresta antiga
                F[old_forest].delete_edge(u, vv)
                # Adiciona aresta na floresta i com o peso apropriado
                F[i].add_edge(u, vv, edge_weights[frozenset((u, vv))])
                # Atualização incremental: une u e vv na partição da floresta i
                partition[i].union(u, vv)
                # Rotaciona as variáveis para a próxima iteração da sequência aumentante
                e, edge_index[fe], i = edge_label[fe], i, edge_index[fe]
                fe = frozenset(e)

            u, vv = tuple(e)
            F[i].add_edge(u, vv, edge_weights[frozenset(e)])
            edge_index[frozenset(e)] = i
            partition[i].union(u, vv)
        else:
            partition[0].union(x, y)

    res = [F[i] for i in range(1, k + 1) if F[i].size() == G.order() - 1]

    if len(res) != k:
        raise ValueError("There is no solution!")

    for f in res:
        for u, v, label in f.edges(labels=True):
            f.set_edge_label(u, v, edge_weights[frozenset((u, v))])

    return res
