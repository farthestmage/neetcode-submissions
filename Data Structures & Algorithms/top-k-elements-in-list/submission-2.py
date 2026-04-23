class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        l2=[]
        l1 = [[0, 0] for _ in range(1000)]
        for i in nums:
            l1[i][1]= i
            l1[i][0]+=1
        l1.sort(reverse=True)
        for i in range (k):
            l2.append(l1[i][1])
        return l2