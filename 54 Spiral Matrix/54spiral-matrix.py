class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ls = []
        d = 0
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while (top <= bottom and left <= right):
            if (d == 0):
                for i in range(left, right + 1):
                    ls.append(matrix[top][i])
                top += 1
            elif (d == 1):
                for i in range(top, bottom + 1):
                    ls.append(matrix[i][right])
                right -= 1
            elif (d == 2):
                for i in range(right, left - 1, -1):
                    ls.append(matrix[bottom][i])
                bottom -= 1
            else:
                for i in range(bottom, top - 1, -1):
                    ls.append(matrix[i][left])
                left += 1
            d = (d + 1) % 4
        
        return ls