import algorithms
import data_creation.run_data
import graphstk
import time
import pandas as pd

df = pd.read_pickle("dataset-grafos-trab-final.pkl")

dataset = df['graph']

start = time.time()
run_dataset(dataset, modified_kruskal)
end = time.time()

print(f"Tempo de execução (Kruskal): {end - start} segundos")

start = time.time()
run_dataset(dataset, edge_disjoint_spanning_trees)
end = time.time()

print(f"Tempo de execução (Roskind-Tarjan): {end - start} segundos")
