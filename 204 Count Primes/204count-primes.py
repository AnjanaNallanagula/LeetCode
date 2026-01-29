class Solution:
    def countPrimes(self, n: int) -> int:
        if (n == 0 or n == 1):
            return 0
        
        ls = [True for i in range(n)]
        ls[0] = False
        ls[1] = False

        for i in range(2, n):
            if (ls[i] == True):
                j = i * i

                while (j < n):
                    ls[j] = False
                    j += i
        
        count = sum(ls)

        return count