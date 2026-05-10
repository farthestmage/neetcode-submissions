class Solution:
    def rob(self, nums: List[int]) -> int:
        # how do you check for circular check start index if start index == 0 then skip last 
        cache = [[-1]*2 for _ in range (len(nums))]
        if len(nums) == 1:
            return nums[0]
        def dfs (i ,flag):
            if i >= len(nums) or (flag and i == len(nums) -1):
                return 0 
            if cache[i][flag] != -1 :
                return cache[i][flag]
            adj = dfs(i+1 ,flag)
            skip = dfs(i+2 ,flag or (i == 0)) + nums[i]
            cache[i][flag] = max(adj,skip)            
            return cache[i][flag]
        
        return max(dfs(0 ,True),dfs(1 ,False))
