class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # maximum = 0

        # # O(n^2) time and O(1) space
        # for i in range(0, len(prices)):
        #     for j in range(i+1, len(prices)):
        #         maximum = max(maximum, (prices[j] - prices[i]))


        # return maximum


        # two pointer method
        l, r = 0 , 1
        maximum = 0


        while r < len(prices):
            if prices[l] < prices[r]:
                maximum = max(maximum, (prices[r] - prices[l]))
            else:
                l = r
            r = r + 1
        
        return maximum

        