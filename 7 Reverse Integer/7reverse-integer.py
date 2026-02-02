class Solution:
    def reverse(self, x: int) -> int:
        flag = False

        if (x < 0):
            flag = True
            x *= -1
        
        n = 0

        while (x != 0):
            r = x % 10
            n = n * 10 + r
            x //= 10
        
        if (flag == True):
            n *= -1
        
        if (n < -2 ** 31 or n > 2 ** 31 - 1):
            return 0
        return n