def minCostConnectNodes(N, connections):
    if N == 0:
        return 0
    if len(connections) < N-1:
        return -1
    connections.sort(key=lambda x: x[2])
    
    uf = UnionFind(N)
    total_cost = 0
    edges_used = 0
    
    for u, v, cost in connections:
        if uf.union(u, v):
            total_cost += cost
            edges_used += 1
            
    if edges_used == N-1:
        return total_cost 
    else:
        return -1
        
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.num_components = n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.num_components -= 1
            return True
        return False