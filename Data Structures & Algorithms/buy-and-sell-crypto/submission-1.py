class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # same min selling price and max buying price after selecting a min ??
        maxP = 0 
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP,sell-minBuy)
            minBuy = min(minBuy,sell)
        return maxP