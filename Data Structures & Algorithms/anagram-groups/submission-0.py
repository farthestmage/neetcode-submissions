def ana(s: str,t: str):
        if len(s)!= len(t):
            return False
        hashms={}
        hashmt={}
        for i in range (len(s)):
            hashms[s[i]]=1+hashms.get(s[i],0)
            hashmt[t[i]]=1+hashmt.get(t[i],0)
        return hashms == hashmt
def anagrmp(l: List[str],s: str):
        if len(l)== 0:
            l.append([s])
            return 0
        for i in range(len(l)):
            if  ana(l[i][0],s):
                l[i].append(s)
                return 0
        l.append([s])
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=[]
        for i in range (len(strs)):
            anagrmp(l,strs[i])
        return l


    
            
    