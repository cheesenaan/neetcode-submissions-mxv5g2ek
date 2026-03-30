class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # find min and max
        # if max - min > 0 return max-min else 0

        profit = 0

        for i in range(len(prices)):
            arr = prices[i:]
            buy = prices[i]
            sell = max(arr)
            p = sell - buy
            profit = max(profit, p)


        return profit

       