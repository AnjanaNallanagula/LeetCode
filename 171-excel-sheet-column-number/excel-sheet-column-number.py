class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        p = 0
        n = 0

        for i in columnTitle[::-1]:
            val = ord(i) - 65 + 1
            n += (26 ** p) * val
            p += 1
        
        return n