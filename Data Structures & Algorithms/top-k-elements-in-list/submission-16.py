class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # top k idea is basic we need to return top 2 common element 
        # Step 1 count number of each element then create a bucket map based
        # on pointing of lenght of return of res list 
        d1 = {}
        for i in nums:
            d1[i] = 1 + d1.get(i,0)
        r = [[] for _ in range(len(nums)+1)]
        for key,value in d1.items():
            r[value].append(key)
        res = []
        for i in range (len(r)-1,-1,-1):
            for j in r[i]:
                res.append(j)
                if len(res) == k:
                    return res
        return res