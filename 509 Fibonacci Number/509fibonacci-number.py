class Solution:
    def fib(self, n: int) -> int:
        if (n == 0 or n == 1):
            return n
        
        ls = [0 for i in range(n+1)]

        ls[1] = 1

        for i in range(2, len(ls)):
            ls[i] = ls[i-1] + ls[i-2]
        
        return ls[n]