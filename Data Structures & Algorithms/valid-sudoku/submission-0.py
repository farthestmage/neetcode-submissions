class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #row checker
        #O[n^2]
        for i in board:
            a=[1]*10
            for j in i:
                if j!= ".":
                    if a[int(j)]<2:
                        a[int(j)]+=1
                    else:
                        return False
        #column checker
        for i in range(9):
            a=[1]*10
            for j in range(9):
                if board[j][i] != ".":
                    if a[int(board[j][i])]<2:
                        a[int(board[j][i])]+=1
                    else:
                        return False
        #box checker
        j=k=0
        l=m=3
        for b in range(3):
            for c in range(3):
                a=[1]*10
                #acess single box
                for d in range(j,l):
                    for e in range(k,m):
                        if board[d][e] != ".":
                            if a[int(board[d][e])]<2:
                                a[int(board[d][e])]+=1
                            else:
                                return False
                k=k+3
                m=m+3
            k=0
            m=3
            j=j+3
            l=l+3    
        return True
