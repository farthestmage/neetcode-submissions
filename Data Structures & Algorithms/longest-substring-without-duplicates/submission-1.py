class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        d1 = {}
        longest = 1
        l,r = 0,1
        d1[s[l]] = 0
        while r< len(s):
            if s[r] in d1:
                l = max(d1[s[r]] + 1, l)
                
            d1[s[r]] = r
            
            longest = max(r-l+1,longest)
            r+=1
        return longest