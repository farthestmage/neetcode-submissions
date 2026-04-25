class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        l1=[]
        nums = list(set(nums))
        nums.sort()
        l1.append(nums[0])
        res = len(l1)
        for i in range(1,len(nums)):
            if nums[i] - nums[i-1] == 1:
                l1.append(nums[i])
            else:
                l1 = []
                l1.append(nums[i])
            res = max(res,len(l1))
        return res
