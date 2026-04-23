class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        postfix=[]
        for i in range(len(nums)):
            if len(prefix) == 0:
                prefix.append(nums[i])
                postfix.append(nums[len(nums)-1-i])
            else:
                prefix.append(nums[i]*prefix[i-1])
                postfix.append(nums[len(nums)-1-i]*postfix[i-1])
        postfix.reverse()
        res=[]
        for i in range(len(nums)):
            if i==0:
                res.append(postfix[1])
            elif i== len(nums)-1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1]*postfix[i+1])
        return res

