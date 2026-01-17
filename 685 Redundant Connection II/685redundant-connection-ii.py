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
    
    def isValidGraph(self, edges, parent, rank, index = -1):
        for i in range(len(edges)):
            if (i == index):
                continue
            
            result = self.union(edges[i][0], edges[i][1], parent, rank)

            if (result == False):
                return (False, edges[i])
        
        return True
    
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [0 for i in range(n + 1)]
        in_degree = [0 for i in range(n + 1)]
        node = -1

        for i in range(n):
            in_degree[edges[i][1]] += 1
            
            if (in_degree[edges[i][1]] == 2):
                node = edges[i][1]

        if (node == -1):
            return self.isValidGraph(edges, parent, rank)[1]
        else:
            for i in range(len(edges) - 1, -1 , -1):
                parent = [i for i in range(n + 1)]
                rank = [0 for i in range(n + 1)]
                
                if (edges[i][1] == node):
                    if (self.isValidGraph(edges, parent, rank, i) == True):
                        return edges[i]