class Solution:
    def isValid(self, n):
        ls = [0, 1, 5, -1, -1, 2, 9, -1, 8, 6]
        num = n
        m = 0
        p = 1
        
        while (num != 0):
            d = num % 10
            
            if (ls[d] == -1):
                return False
            
            m = ls[d] * p + m
            p *= 10
            num //= 10
        
        if (n == m):
            return False
        return True
    
    def rotatedDigits(self, n: int) -> int:
        count = 0
        
        for i in range(1, n + 1):
            if (self.isValid(i) == True):
                count += 1
        
        return count