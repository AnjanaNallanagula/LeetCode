class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        n3 = len(s3)

        if ((n1 + n2) != n3):
            return False
        
        mat = [[False for j in range(n2 + 1)] for i in range(n1 + 1)]
        mat[0][0] = True

        for i in range(1, n1 + 1):
            mat[i][0] = ((s1[i-1] == s3[i-1]) and mat[i-1][0])
        
        for j in range(1, n2 + 1):
            mat[0][j] = ((s2[j-1] == s3[j-1]) and mat[0][j-1])
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                k = i + j

                mat[i][j] = (((s1[i-1] == s3[k-1]) and mat[i-1][j]) or ((s2[j-1] == s3[k-1]) and mat[i][j-1]))
        
        return mat[n1][n2]