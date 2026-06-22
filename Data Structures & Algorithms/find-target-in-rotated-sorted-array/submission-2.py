class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pivot
        l,r = 0,len(nums)-1
        while l< r:
            m = l + (r-l)//2
            if nums[m] > nums[r]:
                l = m+1
            else :
                r = m
        pivot = l
        # Check which section to check
        l , r = 0,len(nums)-1
        if target>=nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot
        while l<=r:
            mid = l+ (r-l)//2
            if nums[mid] == target:
                return mid
            if nums[mid]> target:
                r = mid -1
            else:
                l = mid+1

        return -1 
