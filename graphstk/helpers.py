from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as mcolors


def plotting_MSTs(G,trees):
    pos = nx.spring_layout(G)
    # Get a dictionary of all CSS4 named colors
    named_colors_dict = mcolors.CSS4_COLORS

    # Extract the color names into a list
    colors = list(named_colors_dict.keys())

    for i, tree in enumerate(trees, 1):
        nx.draw_networkx_edges(tree,pos,edge_color=colors[i-1],width = 0.5, alpha=1)
    nx.draw_networkx_nodes(G,pos, alpha=1, node_size = 6, node_color='m')
    plt.show()
  
def BFS_edges(G, source):
    visited = set([source])
    queue = deque([source])
    while queue:
        u = queue.popleft()
        for v in G.neighbors(u):
            if v not in visited:
                visited.add(v)
                queue.append(v)
                yield (u, v)

def to_networkx_graph(g):
    nx_g = nx.Graph()
    # adiciona os nós
    nx_g.add_nodes_from(g.nodes())
    # adiciona as arestas com label/peso, se houver
    for u, v, label in g.edge_iterator(labels=True):
        if label is not None:
            nx_g.add_edge(u, v, weight=label)
        else:
            nx_g.add_edge(u, v)
    return nx_g

def from_networkx_graph(nx_graph):
    custom_g = Graph()
    for node in nx_graph.nodes():
        custom_g.add_vertex(node)
    for u, v, data in nx_graph.edges(data=True):
        label = data.get('weight') if 'weight' in data else None
        custom_g.add_edge(u, v, label)
    return custom_g
