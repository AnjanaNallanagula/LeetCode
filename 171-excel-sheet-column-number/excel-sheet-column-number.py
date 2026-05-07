class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        n = 0
        p = 0

        for i in range(len(columnTitle) - 1, -1, -1):
            d = ord(columnTitle[i]) - ord("A") + 1
            n += (d * pow(26, p))
            p += 1
        
        return n