class Solution:
    def minCost(self, n, edges):
        cost = 0
        count = 0
        parent = [i for i in range(n)]
        rank = [0 for i in range(n)]

        def find(i):
            if (i == parent[i]):
                return i
            parent[i] = find(parent[i])
            return parent[i]
        
        def union(u, v):
            u_rep = find(u)
            v_rep = find(v)

            if (u_rep != v_rep):
                if (rank[u_rep] > rank[v_rep]):
                    parent[v_rep] = u_rep
                elif (rank[v_rep] > rank[u_rep]):
                    parent[u_rep] = v_rep
                else:
                    parent[v_rep] = u_rep
                    rank[u_rep] += 1
                return True
            return False
        
        for u, v, w in edges:
            if (union(u, v)):
                cost += w
                count += 1
            if (count == n - 1):
                break
        
        return cost
    
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                d = abs(x2 - x1) + abs(y2 - y1)
                edges.append((i, j, d))
        
        edges.sort(key = lambda i: i[2])
        
        return self.minCost(n, edges)