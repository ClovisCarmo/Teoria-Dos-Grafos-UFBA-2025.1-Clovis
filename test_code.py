import algorithms
import data_creation.run_data
import graphstk
import time

start = time.time()
run_dataset(dataset_total, modified_kruskal)
end = time.time()

print(f"Tempo de execução: {end - start} segundos")
