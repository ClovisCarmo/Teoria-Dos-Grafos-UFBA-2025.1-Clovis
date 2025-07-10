import algorithms
import data_creation.run_data
import graphstk
import time
import pandas as pd

df = pd.read_csv("dataset-grafos-trab-final.csv")

dataset = df['graph']

start = time.time()
run_dataset(dataset, modified_kruskal)
end = time.time()

print(f"Tempo de execução: {end - start} segundos")
