class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l=defaultdict(list)
        for i in (strs):
            l1=[0]*26

            for c in i:
                l1[ord(c)-ord("a")]+= 1
            l[tuple(l1)].append(i)
        return l.values()


    
            
    