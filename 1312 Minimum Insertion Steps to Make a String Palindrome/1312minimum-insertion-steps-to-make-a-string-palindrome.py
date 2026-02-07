class Solution:
    def minInsertions1(self, i, j, s, mat):
        if (i >= j):
            return 0
        if (mat[i][j] != -1):
            return mat[i][j]
        
        if (s[i] == s[j]):
            mat[i][j] = self.minInsertions1(i + 1, j - 1, s, mat)
        else:
            mat[i][j] = 1 + (min(self.minInsertions1(i + 1, j, s, mat), self.minInsertions1(i, j - 1, s, mat)))

        return mat[i][j]
    
    def minInsertions(self, s: str) -> int:
        mat = [[-1 for j in range(len(s))] for i in range(len(s))]

        return self.minInsertions1(0, len(s) - 1, s, mat)