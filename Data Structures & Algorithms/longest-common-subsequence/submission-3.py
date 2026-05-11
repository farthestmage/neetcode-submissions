class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # pick the minimum length check for first charactar true good move hold one pointer
        memo = {}
        def comSUB(i,j) -> int:
            # always assume str1 is the smaller one 
            if i == len(text1) or j == len(text2):
                return 0
            if (i,j) in memo:
                return memo[(i,j)]
            if text1[i] == text2[j]:
                memo[(i,j)] = 1 + comSUB(i+1,j+1)
            else:
                memo[(i,j)]=max(comSUB(i,j+1),comSUB(i+1,j))

            return  memo[(i,j)]
        return comSUB(0,0)