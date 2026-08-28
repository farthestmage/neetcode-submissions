class Solution:
    def rob(self, nums: List[int]) -> int:
        memo= {}
        def dfs(i,n):
            if i>=n:
                return 0
            if i in memo:
                return memo[i]
            memo[i] = nums[i] + max(dfs(i+2,n),dfs(i+3,n))
            return memo[i]
        return max(dfs(0,len(nums)),dfs(1,len(nums)))