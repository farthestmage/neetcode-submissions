class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def calculateRate(piles:List[int],rateofEat:int) ->int:
            res = 0
            for pile in piles:
                res += (pile+rateofEat-1)//rateofEat
            return res

        left,right = 1 ,max(piles)
        ans = right 
        while left<=right:
            mid = left +(right-left) // 2
            totaltime = calculateRate(piles,mid)
            if totaltime<=h:
                right = mid -1
                ans = mid
            else:
                left = mid+1
        return ans