class Solution:
    def tribonacci(self, n: int) -> int:
        if (n == 0):
            return 0
        if (n == 1 or n == 2):
            return 1
            
        ls = [-1 for i in range(n + 1)]
        ls[0] = 0
        ls[1] = 1
        ls[2] = 1

        for i in range(3, n + 1):
            ls[i] = ls[i - 1] + ls[i - 2] + ls[i - 3]
        
        return ls[n]