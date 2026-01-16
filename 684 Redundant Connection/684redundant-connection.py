class Solution:
    def find(self, u, parent):
        if (u == parent[u]):
            return u
        
        parent[u] = self.find(parent[u], parent)

        return parent[u]
    
    def union(self, u, v, parent, rank):
        u_rep = self.find(u, parent)
        v_rep = self.find(v, parent)

        if (u_rep == v_rep):
            return False
        
        if (rank[u_rep] > rank[v_rep]):
            parent[v_rep] = u_rep
        elif (rank[v_rep] > rank[u_rep]):
            parent[u_rep] = v_rep
        else:
            parent[v_rep] = u_rep
            rank[u_rep] += 1
        
        return True
    
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [0 for i in range(n + 1)]
        ls = []

        for i in edges:
            result = self.union(i[0], i[1], parent, rank)

            if (result == False):
                ls = i
        
        return ls