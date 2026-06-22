class Solution:
    def findMin(self, nums: List[int]) -> int:
        # step 1 check the difference since
        # Check half  note for min values 
        l,r = 0 , len(nums)-1
        res = 10000
        while l<=r:
            if nums[l]< nums [r]:
                res = min(res,nums[l])
                break
            mid = l + (r-l)//2
            res = min(res,nums[mid])
            if nums[mid]>=nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return res