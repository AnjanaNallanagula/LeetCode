class Solution:
    def reverseBits(self, n: int) -> int:
        b = ""

        while n:
            r = n % 2
            b += str(r)
            n //= 2
        
        if (len(b) < 32):
            d = 32 - len(b)
            b = b + "0" * d
        
        p = 0
        m = 0

        for i in range(len(b) - 1, -1, -1):
            m += (2 ** p) * int(b[i])
            p += 1
        
        return m