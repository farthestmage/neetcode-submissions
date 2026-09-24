class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}
        for i in nums:
            d1[i] = 1 + d1.get(i,0)
        
        rev = defaultdict(list)
        for key,value in d1.items():
            rev[value].append(key)
        
        l1 = []
        for i in sorted(rev.keys(),reverse = True):
            for n in rev[i]:
                l1.append(n)
                if len(l1) == k:
                    return l1
        return l1