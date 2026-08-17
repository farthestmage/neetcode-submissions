class Solution:
    def jump(self, nums: List[int]) -> int:
        # Return number of Counts ?? min number of jumps same idea every potential
        # Choice but return min of count use memo for index.
        memo = {}
        res = float('inf')
        def dfs(i,res):
            if i in memo:
                return memo[i]
            if i == len(nums) - 1:
                return 0
            end = min(len(nums)-1,i+nums[i])
            for j in range (i+1,end+1):
                res = min(1+dfs(j,res),res)
            memo[i] = res
            return res
        return dfs(0,res)
            
