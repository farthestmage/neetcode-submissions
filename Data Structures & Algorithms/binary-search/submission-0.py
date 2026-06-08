class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Simple binary search 
        if len(nums) == 0:
            return -1
        
        def recurr(start,end,target):
            if end>= start:
                mid = start +(end-start)//2

                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    return recurr(mid+1,end,target)
                else:
                    return recurr(start,mid-1,target)
            else:
                return -1 
        return recurr(0,len(nums)-1,target)