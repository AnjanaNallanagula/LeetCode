class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        n = len(palindrome)

        if (n == 1):
            return ""
        
        j = -1

        for i in range(n // 2):
            if (palindrome[i] != "a"):
                j = i
                break
        
        if (j == -1):
            for i in range(n - 1, n // 2 - 1, -1):
                if (palindrome[i] != "b"):
                    j = i
                    break
            
            s = palindrome[:j] + "b" + palindrome[j + 1:]
        else:
            s = palindrome[:j] + "a" + palindrome[j + 1:]

        return s