class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        L=[]
        a=list(t)
        for i in s:
            for j in range (len (a)):
                if i == a[j]:
                    L.append(i)
                    del a[j]
                    break
        if len(L)== len(s):
            return True
        return False

