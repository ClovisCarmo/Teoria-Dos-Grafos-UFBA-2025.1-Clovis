from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

class DisjointSet:
    def __init__(self, elements=None):
        self.parent = {}
        self.rank = {}
        if elements:
            for e in elements:
                self.parent[e] = e
                self.rank[e] = 0

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
