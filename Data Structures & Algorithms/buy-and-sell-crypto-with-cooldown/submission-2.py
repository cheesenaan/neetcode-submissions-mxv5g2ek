class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # at each day, either buy/sell or cooldown
        # buy -> i + 1
        # sell -> i+2 for cooldown
        hp = {} # (i,buy?) -> max_profit
        
        def dfs(i, buy):
            if i >= len(prices):
                return 0

            if (i,buy) in hp:
                return hp[(i,buy)]
            
            cooldown = dfs(i+1, buy)
            
            if buy:
                buy_profit = dfs(i+1, not buy) - prices[i]
                hp[(i, buy)] = max(buy_profit, cooldown)
            else:
                sell_profit = dfs(i+2, not buy) + prices[i]
                hp[(i, buy)] = max(sell_profit, cooldown)
            
            return hp[(i, buy)]

        return dfs(0, True)