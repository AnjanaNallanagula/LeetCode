class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.mat = [[0 for j in range(m + 1)] for i in range(n + 1)]
        
        for i in range(n):
            prefix = 0
            for j in range(m):
                prefix += matrix[i][j]
                self.mat[i + 1][j + 1] = prefix + self.mat[i][j + 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        sum1 = self.mat[row2][col2] - self.mat[row1 - 1][col2] - self.mat[row2][col1 - 1] + self.mat[row1 - 1][col1 - 1]

        return sum1

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)