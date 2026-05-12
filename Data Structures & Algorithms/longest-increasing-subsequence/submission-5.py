class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # PROBLEM here is with numbers  just check the subsequence should increase
        # understanding the dp max of both
        n = len(nums)
        dp =[1] * n
        for i in range (n):
            for j in range(i):
                if nums[j]<nums[i]:
                    dp[i] = max(dp[i],1+dp[j])
        return max(dp)