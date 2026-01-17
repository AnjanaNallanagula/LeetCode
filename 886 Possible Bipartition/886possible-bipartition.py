from collections import deque

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adj = [[] for i in range(n + 1)]

        for i in dislikes:
            adj[i[0]].append(i[1])
            adj[i[1]].append(i[0])
        
        ls = [-1 for i in range(n + 1)]
        s = set()

        for i in range(1, n + 1):
            if (i not in s):
                q = deque([])
                q.append(i)
                ls[i] = 0

                while (len(q) != 0):
                    node = q.popleft()
                    s.add(node)

                    for j in adj[node]:
                        if (ls[j] == -1):
                            ls[j] = 1 - ls[node]
                            q.append(j)
                        elif (ls[j] == ls[node]):
                            return False
        
        return True