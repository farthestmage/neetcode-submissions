class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d1 = {}
        for i in nums:
            d1[i] = 1 + d1.get(i,0)

        freq = [[] for i in range(len(nums)+1)]
        for key,value in d1.items():
            freq[value].append(key)
        l1 = []
        for i in range (len(freq)-1 , 0 ,-1):
            for n in freq[i]:
                l1.append(n)
                if len(l1) == k:
                    return l1
        return l1