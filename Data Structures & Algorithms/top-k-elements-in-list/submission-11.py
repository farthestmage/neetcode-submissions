class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}
        for i in nums:
            if i in d1:
                d1[i] +=1
            else:
                d1[i] = 1
        rev= defaultdict(list)
        for key,value in d1.items():
            rev[value].append(key)
        l1=[]
        for i in (sorted(rev.keys(),reverse=True)):
            for n in rev[i]:
                l1.append(n)
                if len(l1)==k:
                    return l1
        return l1