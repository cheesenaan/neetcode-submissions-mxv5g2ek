class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maximum = 0

        for i in range(0, len(prices)):
            for j in range(i+1, len(prices)):
                maximum = max(maximum, (prices[j] - prices[i]))


        return maximum
        