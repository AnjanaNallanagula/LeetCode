class Solution:
    def confusingNumber(self, n: int) -> bool:
        ls = [0, 1, -1, -1, -1, -1, 9, -1, 8, 6]
        num = n
        m = 0
        p = 10
        
        while (num != 0):
            d = num % 10
            
            if (ls[d] == -1):
                return False
            
            m = (m * 10 + ls[d])
            num //= 10
        
        if (n == m):
            return False
        return True