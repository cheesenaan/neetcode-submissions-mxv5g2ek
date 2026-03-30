class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        profit = 0

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            p = sell - buy
            
            if p > 0:
                profit = max(profit, p)
            else:
                l = r

            r = r + 1

        return profit

        