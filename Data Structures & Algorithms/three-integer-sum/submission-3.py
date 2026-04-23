class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        b=[]
        
        for i in range (len (nums)-2):
            left,right=i+1,len(nums)-1
            if nums[i]in b:
                continue
            else:
                b.append(nums[i])
                while left<right:
                    if nums[left]+nums[right] > (-nums[i]):
                        right=right-1
                    elif nums[left]+nums[right]<(-nums[i]):
                        left=left+1
                    else:
                        res.append([nums[i],nums[left],nums[right]])
                        left=left+1
                        right = right -1
                        while nums[left]== nums[left-1] and left<right:
                            left+=1
                            
                        
        return res
