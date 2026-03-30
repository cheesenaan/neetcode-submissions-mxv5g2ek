class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # at each day we can either buy/sell or cooldown
        # buying -> i + 1
        # sell -> i + 2
        hp = {} # (i,buying?) -> max profit

        def dfs(i, buying):
            if i >= len(prices):
                return 0

            if (i,buying) in hp:
                return hp[(i, buying)]

            cooldown_profit  = dfs(i+1, buying)
            if buying:
                buy_profit = dfs(i+1, not buying) - prices[i]
                hp[(i, buying)] = max(buy_profit, cooldown_profit)
            else:
                sell_profit = dfs(i+2, not buying) + prices[i]
                hp[(i, buying)] = max(sell_profit, cooldown_profit)

            return hp[(i, buying)]
        
        return dfs(0, True)
        