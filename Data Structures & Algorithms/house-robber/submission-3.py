class Solution:
    def rob(self, nums: List[int]) -> int:
         # never  +1 starting index can be 0 or 1 max of that 
         # you can + 2 it or +3 it at max 

        cache = [-1] * len(nums)

        def dfs (i):
            if i >= len(nums):
                return 0 
            if cache[i] != -1 :
                return cache[i]
            
            cache[i] = max(dfs(i+1),nums[i] + dfs(i+2))
            return cache[i]
        
        return (dfs(0))
