from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = [[] for i in range(numCourses)]
        in_degree = [0 for i in range(numCourses)]

        for u, v in prerequisites:
            adj[v].append(u)
            in_degree[u] += 1
        
        q = deque()

        for i in range(numCourses):
            if (in_degree[i] == 0):
                q.append(i)
        
        ls = []

        while (len(q) != 0):
            u = q.popleft()
            ls.append(u)

            for v in adj[u]:
                in_degree[v] -= 1

                if (in_degree[v] == 0):
                    q.append(v)
        
        if (len(ls) == numCourses):
            return True
        return False