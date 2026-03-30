class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP = 0
        l, r = 0, 1

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            profit = sell - buy
            maxP = max(maxP, profit)

            if profit < 0:
                l = r
            r += 1

        return maxP

        