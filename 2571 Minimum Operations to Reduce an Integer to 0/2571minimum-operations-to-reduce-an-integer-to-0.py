class Solution:
    def minOperations(self, n: int) -> int:
        @cache
        def dfs(x):
            if (x & (x - 1) == 0):
                return 1
            
            d = x & (-x)

            return (1 + min(dfs(x + d), dfs(x - d)))
        
        return dfs(n)