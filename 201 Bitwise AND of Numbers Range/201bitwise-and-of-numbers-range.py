class Solution:
    def msb(self, num):
        p = -1
        while (num > 0):
            num = num >> 1
            p += 1
        return p
    
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        p = 0
        while (left > 0 and right > 0):
            n = self.msb(left)
            m = self.msb(right)
            if (n != m):
                break
            p += (1 << n)
            left -= (1 << n)
            right -= (1 << m)
        return p