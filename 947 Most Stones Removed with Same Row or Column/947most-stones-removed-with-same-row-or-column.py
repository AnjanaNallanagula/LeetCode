class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        s = set()
        n = len(stones)
        count = 0
        
        def dfs(i):
            s.add(i)
            
            for j in range(n):
                if (j not in s):
                    if (stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]):
                        dfs(j)
        
        for i in range(n):
            if (i not in s):
                dfs(i)
                count += 1
        
        d = n - count
        
        return d