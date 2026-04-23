class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count= {}
        freq = [[] for i in range(len(nums)+1)]
        for n in nums:
            count[n]=1+count.get(n,0)
        
        for i in (count.keys()):
            freq[count[i]].append(i)

        l1=[]
        for i in range (len(freq)-1,0,-1):
          for n in freq[i]:
            l1.append(n)
            if len(l1)==k:
                return l1
        return l1