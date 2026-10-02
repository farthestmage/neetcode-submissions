class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Simple idea set bna do usmai utha utha kr check kro agar previous element 
        #hai ya nhi 
        longest = 0
        a = set(nums)
        for i in nums:
            if i-1 not in a:
                l = 0
                while (l+i) in a:
                    l+=1
                longest = max(longest,l)
        return longest