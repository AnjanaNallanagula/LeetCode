class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        node_count = [1 for i in range(n)]
        edge_count = [0 for i in range(n)]

        def find(u):
            if (parent[u] == u):
                return u
            parent[u] = find(parent[u])
            return parent[u]
        
        def union(u, v):
            u_rep = find(u)
            v_rep = find(v)

            if (u_rep == v_rep):
                edge_count[u_rep] += 1
            else:
                parent[v_rep] = u_rep
                node_count[u_rep] += node_count[v_rep]
                edge_count[u_rep] += edge_count[v_rep] + 1

        for u, v in edges:
            union(u, v)

        result = 0

        for i in range(n):
            if (parent[i] == i):
                e = edge_count[i]
                n = node_count[i]

                if (e == (n * (n - 1) // 2)):
                    result += 1

        return result