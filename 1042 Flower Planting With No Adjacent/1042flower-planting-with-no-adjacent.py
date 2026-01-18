class Solution:
    def isSafe(self, i, k, adj, ls):
        for j in adj[i]:
            if (ls[j] != -1 and ls[j] == k):
                return False
        
        return True
    
    def gardenNoAdj1(self, i, n, adj, ls):
        if (i == n):
            return True
        
        for k in range(1, 5):
            if (self.isSafe(i, k, adj, ls) == True):
                ls[i] = k

                if (self.gardenNoAdj1(i + 1, n, adj, ls) == True):
                    return True
                
                ls[i] = -1
        
        return False
    
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        adj = [[] for i in range(n)]
        ls = [-1 for i in range(n)]

        for i in paths:
            adj[i[0] - 1].append(i[1] - 1)
            adj[i[1] - 1].append(i[0] - 1)
        
        self.gardenNoAdj1(0, n, adj, ls)

        return ls