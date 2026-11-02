class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d1 = {"2":"abc","3":"def","4":"ghi","5":"jkl"
              ,"6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
        }

        #stack = []
        res = []
        def dfs(i,j):

            if len(j) == len(digits):
                res.append(j)
                return
            for c in d1[digits[i]]:
                dfs(i+1,j+c)
        if digits:
            dfs(0,"")

        return res