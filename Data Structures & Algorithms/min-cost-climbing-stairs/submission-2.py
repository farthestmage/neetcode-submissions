class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        def dfs(i,n):
            if i == n:
                return 0
            if i>n:
                return float('inf')
            if i in memo:
                return memo[i]
            memo[i] = cost[i] + min(dfs(i+1,n),dfs(i+2,n))
            return memo[i]
        return min(dfs(0,len(cost)),dfs(1,len(cost)))