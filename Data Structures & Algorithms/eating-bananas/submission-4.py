class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Sort all of the elements of array max time 
        #piles.sort()
        left ,right = 1 , max(piles)
        ans = right
        while left<=right:
            mid = left + (right - left )// 2
            totalTime = sum(math.ceil(pile/mid)for pile in piles)
            if totalTime <= h:
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
         
        return ans
