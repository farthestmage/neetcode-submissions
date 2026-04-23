class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        hasdic={}
        for i in range (len(nums)):
            if target - nums[i] not in hasdic.keys():
                hasdic[nums[i]]= i
            else:
                l.append(hasdic[target-nums[i]])
                l.append(i)
                return l
