class Solution:
    def palindrome1(self, s, i, j):
        while (i < j):
            if (s[i] != s[j]):
                return False
            
            i += 1
            j -= 1
        
        return True
    
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while (i < j):
            if (s[i] != s[j]):
                return (self.palindrome1(s, i + 1, j) or self.palindrome1(s, i, j - 1))

            i += 1
            j -= 1

        return True 