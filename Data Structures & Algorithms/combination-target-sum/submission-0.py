class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Unique combinations where it equals to target ? 
        # So we choose a number or not check for a summ
        # frequency map 
        # on we choose number A 1 time then dfs without increasing the index
        #  Increasing the sum of A n times till the value if the sum value greater than target don't do nothing

        res = []
        subset = []
        # map (int,freq) map
        
        def dfs(i,total):
            
            if total == target:
                res.append(list(subset.copy()))
                return
            if i>=len(nums) or total > target:
                return
            
            subset.append(nums[i])
            dfs(i,total+nums[i])
            subset.pop()
            dfs(i+1,total)

        dfs(0,0)
        return res

