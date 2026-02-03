class Solution:
    def isSafe(self, k, row, col, board, rows, cols, boxes):
        if (k in rows[row]):
            return False
        if (k in cols[col]):
            return False
        
        index = (row // 3) * 3 + (col // 3)

        if (k in boxes[index]):
            return False
        return True
    
    def solveSudoku1(self, board, rows, cols, boxes):
        for row in range(9):
            for col in range(9):
                if (board[row][col] == "."):
                    for k in "123456789":
                        if (self.isSafe(k, row, col, board, rows, cols, boxes) == True):
                            board[row][col] = k
                            index = (row // 3) * 3 + (col // 3)
                            rows[row].add(k)
                            cols[col].add(k)
                            boxes[index].add(k)

                            if (self.solveSudoku1(board, rows, cols, boxes) == True):
                                return True
                            
                            board[row][col] = "."
                            rows[row].remove(k)
                            cols[col].remove(k)
                            boxes[index].remove(k)
                    
                    return False

        return True
    
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for i in range(9)]
        cols = [set() for j in range(9)]
        boxes = [set() for k in range(9)]

        for i in range(9):
            for j in range(9):
                if (board[i][j] != "."):
                    index = (i // 3) * 3 + (j // 3)
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[index].add(board[i][j])

        self.solveSudoku1(board, rows, cols, boxes)