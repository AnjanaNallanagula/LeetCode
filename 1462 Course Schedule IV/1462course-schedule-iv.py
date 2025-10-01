from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [[] for i in range(numCourses)]
        ls = []

        for i in prerequisites:
            adj[i[0]].append(i[1])
        
        def dfs(i, target, s):
            if (i == target):
                return True
            
            s.add(i)

            for j in adj[i]:
                if (j not in s):
                    if (dfs(j, target, s) == True):
                        return True
            
            return False
            
        for i in queries:
            s = set()

            if (dfs(i[0], i[1], s) == True):
                ls.append(True)
            else:
                ls.append(False)
        
        return ls