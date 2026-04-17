class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(u):
            if (parent[u] == u):
                return u
            
            parent[u] = find(parent[u])

            return parent[u]
        
        def union(u, v):
            u_rep = find(u)
            v_rep = find(v)

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

        for u, v in edges:
            if (union(u, v) == False):
                return False
            
        for i in range(n):
            parent[i] = find(i)
        
        if (len(set(parent)) == 1):
            return True
        return False