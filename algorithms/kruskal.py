def kruskal(edges, n):
  res = []
  st = DisjointSet(elements=range(n))
  i = 0
  l = len(edges)
  while i < l:
    u, v, weight = edges[i]
    x = st.find(u)
    y = st.find(v)

    if x != y:
        res.append((u, v, weight))
        st.union(x, y)
        edges.remove(edges[i])
        l -= 1
    else:
        i += 1

  tree = Graph()
  for edge in res:
    tree.add_edge(*edge)

  return tree, edges

# modified for k spanning trees (the algorithm is NOT correct and will fail to find k in some specific cases)
def modified_kruskal(G,  k, weights=True):
   F = []
   i, n = 0, len(G.adj_list)
   edges = G.order_by_weight()

   while i < k:
    res_i, edges = kruskal(edges, n)
    if len(res_i.edges()) != n-1:
      break

    F.append(res_i)
    i += 1


   res = [F[j] for j in range(i)]
   return res
