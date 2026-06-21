class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Sort all of the elements of array max time 
        #piles.sort()
        left ,right = 1 , max(piles)
        ans = right
        def calcHRS(num:int):
            #l1  = [x for x in piles]
            h=0
            for p in piles:
                h += math.ceil(float(p)/num)
            return h
        while left<=right:
            mid = left + (right - left )// 2
            check = calcHRS(mid)
            if check > h:
                left = mid+1
            else:
                right = mid - 1
                ans = mid
         
        return ans
