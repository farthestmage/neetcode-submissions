class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d1 =set()
        l,r=0,0
        maxLen = 0
        while r<len(s):
            while s[r] in d1:
                d1.remove(s[l])
                l+=1
            d1.add(s[r])
            maxLen=max(maxLen,r-l+1)
            r+=1
        return maxLen