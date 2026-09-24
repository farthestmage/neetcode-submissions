class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # How to create a thinking 
        pre = []
        post = []

        for i in range(len(nums)):
            if i == 0:
                pre.append(nums[i])
                post.append(nums[len(nums)-1-i])
            else:
                pre.append(nums[i]*pre[i-1])
                post.append(nums[len(nums)-1-i]*post[i-1])
        post.reverse()
        res = []
        for i in range(len(nums)):
            if i== 0:
                res.append(post[i+1])
            elif i == len(nums)-1:
                res.append(pre[i-1])
            else:
                res.append(pre[i-1]*post[i+1])
        return res