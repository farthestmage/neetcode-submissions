class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # simple 
        result = max_pro = min_prod = nums[0]
        
        for num in nums[1:]:
            cand = (num,max_pro * num , min_prod*num)
            max_pro = max(cand)
            min_prod = min(cand)
            result = max(max_pro,result)
        return result