class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max1 = float("inf")
        s = ""

        for i in strs:
            if (len(i) < max1):
                max1 = len(i)
                s = i
        
        k = 0

        for i in range(len(s)):
            count = 0

            for j in strs:
                if (i < len(j) and j[i] == s[i]):
                    count += 1

            if (count != len(strs)):
                break
            
            k += 1
        
        return s[:k]