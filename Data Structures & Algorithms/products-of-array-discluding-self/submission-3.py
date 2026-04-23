class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num=1
        zero=0
        for i in nums:
            if i!=0:
                num=num*i
            else:
                zero+=1
        prox=[]
        if zero>1:
            return [0]*len(nums)
        if 0 in nums:
            for i in range(len(nums)):
                if nums[i]== 0:
                    prox.append(num)
                else:
                    prox.append(0)
        else:
            for i in range(len(nums)):
                prox.append(int(num/nums[i]))
        return prox        