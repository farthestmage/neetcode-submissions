class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hasdict={}
        l2=[]
        for i in nums:
            hasdict[i]=1+hasdict.get(i,0)
        heap=[None for _ in range(len(nums)+1)]
        for key,value in hasdict.items():
                if heap[value]==None:
                    heap[value]=[key]
                else:
                    heap[value].append(key)
        for i in range (len(heap)-1,0,-1):
                if heap[i] != None:
                    l2.extend(heap[i])
                    
                if len(l2)==k:
                    break
        return l2    