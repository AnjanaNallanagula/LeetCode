class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ls = [0 for i in range(len(words))]
        for i in range(len(words)):
            p = 0
            for j in words[i]:
                d = ord(j) - ord("a")
                p = p | (1 << d)
            ls[i] = p
        
        max1 = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if (ls[i] & ls[j] == 0):
                    max1 = max(max1, len(words[i]) * len(words[j]))
        return max1