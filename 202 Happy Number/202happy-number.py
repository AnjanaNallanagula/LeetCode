class Solution:
    def isHappy(self, n: int) -> bool:
        if (n == 1):
            return True
        if (n < 10 and n != 1 and n != 7):
            return False
        
        m = 0

        while (n != 0):
            r = n % 10
            m += (r ** 2)
            n //= 10
        
        return self.isHappy(m)