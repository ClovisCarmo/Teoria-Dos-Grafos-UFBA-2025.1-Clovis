def run_dataset(dataset, algorithm):
 for i, G in enumerate(dataset):
    G_graph = from_networkx_graph(G)
    F = algorithm(G_graph, k=26, weights=True)
    print(len(F))
    for j, tree in enumerate(F, 1):
       print(f"Spanning Tree {j} edges:", tree.edges(labels=True))
       total_weight = sum(label for _, _, label in tree.edges(labels=True))
       print(f"Total weight: {total_weight}")

    trees = [to_networkx_graph(tree) for tree in F]

    G_graph = to_networkx_graph(G_graph)

    plotting_MSTs(G_graph,trees)
