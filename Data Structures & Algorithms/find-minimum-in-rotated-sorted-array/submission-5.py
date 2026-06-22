class Solution:
    def findMin(self, nums: List[int]) -> int:
        # step 1 check the difference since
        # Check half  note for min values 
        l,r = 0 , len(nums)-1
        res = 10000
        while l<=r:
            
            mid = l + (r-l)//2
            res = min(res,nums[mid])
            if nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        return res