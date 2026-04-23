class Solution:

    def encode(self, strs: List[str]) -> str:
        stx=""
        for i in strs:
            stx +=str(len(i))+"#"+i
        return stx
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i< len(s):
            j = i
            while s[j]!="#":
                j+=1
            leng= int(s[i:j])
            i=j+1
            j=leng+i
            res.append(s[i:j])
            i=j
        return res


