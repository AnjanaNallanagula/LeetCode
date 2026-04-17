class Solution:
    def longestPalindrome(self, s: str) -> str:
        max1 = -1
        s1 = ""
        
        for i in range(len(s)):
            j = i
            k = i
            
            while (j >= 0 and k < len(s) and s[j] == s[k]):                
                j -= 1
                k += 1
            
            if ((k - j - 1) > max1):
                max1 = (k - j - 1)
                s1 = s[j+1: k]
            
            j = i
            k = i + 1
            
            while (j >= 0 and k < len(s) and s[j] == s[k]):
                j -= 1
                k += 1
            
            if ((k - j - 1) > max1):
                max1 = (k - j - 1)
                s1 = s[j+1: k]
        
        return s1