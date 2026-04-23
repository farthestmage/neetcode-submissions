class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        hashms={}
        hashmt={}
        for i in range (len(s)):
            hashms[s[i]]=1+hashms.get(s[i],0)
            hashmt[t[i]]=1+hashmt.get(t[i],0)
        return hashms == hashmt
