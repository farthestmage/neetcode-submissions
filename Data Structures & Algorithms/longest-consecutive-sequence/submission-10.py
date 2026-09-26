class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in s:
            if i-1 not in s:
                lex = 1
                while (i+lex) in s:
                    lex+=1
                longest = max(longest , lex)
        return longest