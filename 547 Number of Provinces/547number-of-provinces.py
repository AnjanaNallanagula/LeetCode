class Solution:
    def find(self, u, parent):
        if (parent[u] == u):
            return u
        
        parent[u] = self.find(parent[u], parent)

        return parent[u]
    
    def union(self, u, v, parent, rank):
        u_rep = self.find(u, parent)
        v_rep = self.find(v, parent)

        if (u_rep != v_rep):
            if (rank[u_rep] < rank[v_rep]):
                parent[u_rep] = v_rep
            elif (rank[v_rep] < rank[u_rep]):
                parent[v_rep] = u_rep
            else:
                parent[v_rep] = u_rep
                rank[u_rep] += 1
        
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]

        for i in range(n):
            for j in range(n):
                if (isConnected[i][j] == 1):
                    self.union(i, j, parent, rank)

        for i in range(n):
            parent[i] = self.find(i, parent)
        
        count = len(set(parent))

        return count