class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #using hash set 
        s = {}
        for i in range (len(nums)):
            if target - nums[i] in s:
                return [s[target-nums[i]],i]
            s[nums[i]] = i
        return [0,0]