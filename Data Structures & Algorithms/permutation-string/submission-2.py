class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        window_size = len(s1) 
        d1 = {}
        d2 = {}
        for i in s1:
            d1[i] = 1 + d1.get(i,0)

        l,r=0,window_size
        for i in range (l,r):
                d2[s2[i]] = 1 + d2.get(s2[i],0)
        while r<len(s2):
            if d2 == d1:
                return True
            d2[s2[l]] -= 1
            if d2[s2[l]] == 0:
                del d2[s2[l]] 
            d2[s2[r]] = 1 + d2.get(s2[r],0)
            l+=1
            r+=1
            
        return d1 == d2