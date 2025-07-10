from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import random

def add_random_weights(G, max_weight=10):
    for u, v in G.edges():
        G[u][v]['weight'] = random.randint(1, max_weight)

def ensure_min_degree(G, min_degree=4, max_weight=10):
    nodes = list(G.nodes())
    while True:
        low_degree_nodes = [node for node in nodes if G.degree(node) < min_degree]
        if not low_degree_nodes:
            break
        for node in low_degree_nodes:
            needed = min_degree - G.degree(node)
            possible_targets = [n for n in nodes if n != node and not G.has_edge(node, n)]
            random.shuffle(possible_targets)
            for target in possible_targets[:needed]:
                G.add_edge(node, target, weight=random.randint(1, max_weight))
    return G

def generate_graph_with_min_degree(n_nodes=100, min_degree=4, max_weight=10, type_graph='regular', seed=None, p = 0.1):
    if seed is not None:
        random.seed(seed)

    if type_graph == 'regular':
        if n_nodes * min_degree % 2 != 0:
            raise ValueError("Para grafo regular, n_nodes * min_degree deve ser par")
        G = nx.random_regular_graph(min_degree, n_nodes)

    elif type_graph == 'complete':
        G = nx.complete_graph(n_nodes)

    elif type_graph == 'watts_strogatz':
        # k deve ser par e >= min_degree para garantir densidade mínima inicial
        k = max(min_degree, 2 * (min_degree // 2))  # arredonda para par >= min_degree
        p = p  # probabilidade de rewire, pode ser parâmetro depois
        G = nx.watts_strogatz_graph(n_nodes, k, p)

    elif type_graph == 'erdos_renyi':
        # p estimado para gerar conectividade razoável; pode ajustar
        p = p
        G = nx.erdos_renyi_graph(n_nodes, p)

    elif type_graph == 'barabasi_albert':
        m = max(1, min_degree // 2)
        G = nx.barabasi_albert_graph(n_nodes, m)

    # Garante grau mínimo (adiciona arestas se necessário)
    G = ensure_min_degree(G, min_degree, max_weight)

    # Adiciona pesos aleatórios nas arestas existentes (se não foram adicionados no ensure_min_degree)
    add_random_weights(G, max_weight)

    return G

def create_graph_dataset(count=5, sizes=[50, 100, 200, 300, 400], min_degree=4,seed = seed,type_graph = 'regular',p = 0.1):
    graphs = []
    for i, n in enumerate(sizes):
        G = generate_graph_with_min_degree(n_nodes=n, min_degree=min_degree,type_graph=type_graph,p=p)
        graphs.append(G)
    return graphs
