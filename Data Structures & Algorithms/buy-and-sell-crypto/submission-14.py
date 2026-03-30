class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profit = 0
        l, r = 0, 1

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            p = sell - buy
            profit = max(profit, p)

            if p < 0:
                l = r
            r = r + 1

        return profit


        