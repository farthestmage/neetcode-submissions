class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        l1 = []
        for i in strs:
            if len(l1) !=0:
                count=0
                for j in l1:
                    if sorted(j[0]) == sorted(i):
                        j.append(i)
                        count+=1
                        break
                if count==0:
                    l1.append([i])
            else:
                l1.append([i])    
        return l1