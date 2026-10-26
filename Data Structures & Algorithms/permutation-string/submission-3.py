class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)> len(s2):
            return False
        l = 0
        r = len(s1)
        d1 = {}
        for i in s1:
            d1[i] = 1+ d1.get(i,0)
        d2 = {}
        for i in s2[l:r]:
                d2[i] = 1+d2.get(i,0)
        while r<=len(s2): 
            if d2 == d1:
                return True
            d2[s2[l]] -=1
            if d2[s2[l]] == 0:
                del d2[s2[l]]
            l+=1
            if r<len(s2):
                d2[s2[r]] = 1+d2.get(s2[r],0)
            r+=1
        return False 