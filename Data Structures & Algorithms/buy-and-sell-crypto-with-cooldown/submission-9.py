class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        hp = {}
        def dfs(i, buy):
            if i >= len(prices):
                return 0
            
            if (i, buy) in hp:
                return hp[(i, buy)]
            
            cooldown_profit = dfs(i+1, buy)
            if buy:
                buy_max_profit = dfs(i+1, not buy) - prices[i]
                hp[(i, buy)] = max(buy_max_profit, cooldown_profit)
            else:
                sell_profit = dfs(i+2, not buy) + prices[i]
                hp[(i, buy)] = max(sell_profit, cooldown_profit)
            return hp[(i, buy)]

        return dfs(0, True)
        