from collections import deque

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        q = deque([])
        adj = [[] for i in range(n)]
        in_degree = [0 for i in range(n)]

        for i in range(n):
            for j in graph[i]:
                adj[j].append(i)
                in_degree[i] += 1
        
        for i in range(n):
            if (in_degree[i] == 0):
                q.append(i)
        
        ls = []

        while (len(q) != 0):
            i = q.popleft()
            ls.append(i)

            for j in adj[i]:
                in_degree[j] -= 1

                if (in_degree[j] == 0):
                    q.append(j)
        
        ls.sort()

        return ls