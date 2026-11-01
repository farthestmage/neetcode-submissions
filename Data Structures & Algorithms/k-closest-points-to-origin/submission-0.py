class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calcDistance(x1,y1):
            return ((x1-0)**2 + (y1-0)**2)
        
        heap = []

        for i in points:
            heapq.heappush(heap,(-calcDistance(i[0],i[1]),i))

            if len(heap)>k:
                heapq.heappop(heap)
        return [pts  for i,pts in heap]