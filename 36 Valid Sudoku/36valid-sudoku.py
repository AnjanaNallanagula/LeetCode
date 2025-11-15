class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for j in range(9)]
        boxes = [set() for k in range(9)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                if (board[i][j] != "."):
                    k = (i // 3) * 3 + (j // 3)

                    if (board[i][j] in rows[i] or board[i][j] in cols[j] or board[i][j] in boxes[k]):
                        return False
                    
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[k].add(board[i][j])
        
        return True