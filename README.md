# **Teoria-Dos-Grafos-UFBA-2025.1-Clovis**
## Repositorio para o trabalho final de teoria dos grafos do semestre de 2025.1 (Professor: Roberto Freitas Parente)

* Grupo: Clovis Generoso Carmo, Guilherme Barbosa Santanna, Lucca Oliveira Seixas e Rafael Melo Santos
* Abordagem: Algoritmica
* Tema: Encontrar K-arvores geradoras minimas disjuntas por arestas em um grafo conexo
* Artigo de Referencia: A Note on Finding Minimum-Cost Edge-Disjoint Spanning Trees
  * Link ===> https://pubsonline.informs.org/doi/abs/10.1287/moor.10.4.701
* Codigo usado para rodar os testes (tambem possui as implementacoes dos algoritmos de Roskind-Tarjan e Kruskal ---> Grafos_Test_Code.ipynb
___
Para rodar os testes, basta baixar o "Grafos_Test_Code.ipynb" e o "dataset-grafos-trab-final.pkl" para um mesmo diretorio e executar o codigo: 
* A parte com test code pode ser modificada para escolher o algoritmo e o k desejado
* utilize  a funcionalidade *%timeit* (-r para passar o numero de repeticoes, -n para passar numero de loops) na linha onde for testar o tempo de execucao (por default deixamos no run_dataset
* Recomendamos rodar o codigo atraves do google colab. Basta fazer o upload do .ipynb e do .pkl para poder rodar o codigo
* Caso decida rodar o codigo localmente, certifique-se de que o jupyter, python e kernel do ipynb estao devidamente instalados (no VScode, basta instalar as extensoes e o kernel). Se houver necessidade de instalar dependencias para as bibliotecas, basta fazer  "pip install 'nome_da_biblioteca'".
