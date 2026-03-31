class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = [[] for i in range(n)]

        for i in range(n):
            if (manager[i] != -1):
                adj[manager[i]].append(i)
        
        def dfs(node):
            max1 = 0

            for j in adj[node]:
                max1 = max(max1, dfs(j))
            
            return (informTime[node] + max1)
        
        return dfs(headID)