class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Logic is complexxx
        prefix = []
        postfix = []

        for i in range(len(nums)):
            if len(prefix) == 0:
                prefix.append(nums[0])
                postfix.append(nums[-1])
            else:
                prefix.append(prefix[i-1]*nums[i])
                postfix.append(postfix[i-1] * nums[len(nums)-1-i])
        postfix.reverse()
        res = []
        for i in range(len(nums)):
            if i == 0:
                res.append(postfix[i+1])
            elif i == len(nums) - 1:
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1]*postfix[i+1])
        return res