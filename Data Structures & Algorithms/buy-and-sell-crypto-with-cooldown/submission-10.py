class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        hp = {}
        def dfs(i, buy):
            if i >= len(prices):
                return 0

            if (i,buy) in hp:
                return hp[(i,buy)]

            cooldown = dfs(i+1, buy)

            if buy:
                buy_p = dfs(i+1, not buy) - prices[i]
                hp[(i,buy)] = max(buy_p, cooldown)
            else:
                sell_p = dfs(i+2, not buy) + prices[i]
                hp[(i,buy)] = max(sell_p, cooldown)

            return hp[(i,buy)]

        return dfs(0, True)

        