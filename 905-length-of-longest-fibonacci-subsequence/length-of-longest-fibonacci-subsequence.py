class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        mat = [[0 for j in range(n)] for i in range(n)]

        for i in range(n):
            for j in range(i):
                mat[i][j] = 2
        
        d = {arr[i]: i for i in range(n)}
        max1 = 0

        for i in range(2, n):
            for j in range(1, i):
                k = arr[i] - arr[j]

                if (k in d and d[k] < j):
                    mat[i][j] = max(mat[i][j], mat[j][d[k]] + 1)
                    max1 = max(max1, mat[i][j])
        
        if (max1 >= 3):
            return max1
        return 0