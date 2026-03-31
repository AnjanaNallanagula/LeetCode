class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = {}

        for i in range(len(s)):
            d[s[i]] = i
        
        max1 = 0
        ls = []
        j = 0

        for i in range(len(s)):
            max1 = max(max1, d[s[i]])

            if (i == max1):
                ls.append((i - j + 1))
                j = i + 1

        return ls 