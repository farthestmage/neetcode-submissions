class Solution:
    def climbStairs(self, n: int) -> int:
        # Memoization
        memo = {}
        def dfs(i,target):
            if i == target:
                return 1
            if i>target:
                return 0
            if i in memo:
                return memo[i]
            memo[i]=dfs(i+1,target)+dfs(i+2,target)
            return memo[i]
        return dfs(0,n)