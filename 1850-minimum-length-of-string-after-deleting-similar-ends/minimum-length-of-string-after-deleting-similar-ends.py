class Solution:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        n = len(s)

        while (i < j and s[i] == s[j]):
            s1 = s[i]

            while (i <= j and s[i] == s1):
                i += 1
            while (i <= j and s[j] == s1):
                j -= 1
        
        return (j - i + 1)