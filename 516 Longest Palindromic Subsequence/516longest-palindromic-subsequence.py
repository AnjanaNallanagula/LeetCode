class Solution:
    def longestPalindromicSubsequence1(self, s, s1, mat, n1, n2):
        if (n1 == 0 or n2 == 0):
            mat[n1][n2] = 0
        
        if (mat[n1][n2] == -1):
            if (s[n1 - 1] == s1[n2 - 1]):
                mat[n1][n2] = 1 + self.longestPalindromicSubsequence1(s, s1, mat, n1 - 1, n2 - 1)
            else:
                mat[n1][n2] = max(self.longestPalindromicSubsequence1(s, s1, mat, n1 - 1, n2), self.longestPalindromicSubsequence1(s, s1, mat, n1, n2 - 1), self.longestPalindromicSubsequence1(s, s1, mat, n1 - 1, n2 - 1))
        
        return mat[n1][n2]

    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        mat = [[-1 for j in range(len(s) + 1)] for i in range(len(s) + 1)]
        s1 = s[::-1]

        return self.longestPalindromicSubsequence1(s, s1, mat, n, n)