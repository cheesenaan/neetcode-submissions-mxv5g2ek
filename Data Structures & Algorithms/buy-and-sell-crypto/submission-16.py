class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l, r = 0, 1
        profit = 0

        while r < len(prices):
            buy = prices[l]
            sell = prices[r]
            if sell - buy > 0:
                profit = max(profit, (sell-buy))
            else:
                l = r
            r += 1

        return profit

        