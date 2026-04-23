class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for c in range(0,9):
            seen = set()
            for r in range(0,9):
                if board[r][c]==".":
                    continue
                else:
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
                    


       
        for r in range(0,9):
            seen=set()
            for c in range(0,9):
                if board[r][c]==".":
                    continue
                else:
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
       
        for row in range(0,7,3):
            for col in range(0,7,3):
                seen = set()
                for r in range (3):
                    for c in range (3):
                        if board[r+row][c+col]==".":
                            continue
                        else:
                            if board[r+row][c+col] in seen:
                                return False
                            seen.add(board[r+row][c+col])
        return True