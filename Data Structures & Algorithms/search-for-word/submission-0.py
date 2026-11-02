class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Pick a letter check up down right left if down go 1 down
        # if len word same as sliced string or stack compare the word if not 
        # equal return nothing 

        stack = set()

        # i and j board grid and K is the word like first letter 
        def dfs(i,j,k):
            if k == len(word):
                return True
            if (min(i,j)<0 or i>= len(board) or j>=len(board[0]) or word[k] != board[i][j] or (i,j) in stack):
                return False
            stack.add((i,j))
            
            res = (dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or
            dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            )
            stack.remove((i,j))
            return res
        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i,j,0):
                    return True
        return False

