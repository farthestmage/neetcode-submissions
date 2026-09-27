class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxSize = 0
        l=0
        a = set()
        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[l])
                l+=1

            a.add(s[r])
            maxSize = max(maxSize,r-l+1)
        return maxSize