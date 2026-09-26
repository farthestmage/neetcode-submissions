class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for i in nums:
            countMap[i] = 1 + countMap.get(i,0)
        res = []
        bucket = [[] for _ in range(len(nums)+1)]

        for key ,value in countMap.items():
            bucket[value].append(key)
        
        for i in range (len(bucket)-1,0,-1):
            if len(bucket[i])!=0:
                for j in range (len(bucket[i])):
                    res.append(bucket[i][j])
                    if len(res) == k:
                        return res
                    
        return [0,0]