class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d1 = defaultdict(list)
        for i in strs:
            char = [0]*26
            for j in i:
                char[ord(j)-ord('a')] +=1
            d1[tuple(char)].append(i)
        return list(d1.values())