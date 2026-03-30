class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        #################### solution 1 ##############################

        # o(n) time and space
        # top down DP solution using recursion and memoization with O(n) time and space
        # at each day we can either buy/sell or cooldown
        # buying -> i + 1
        # sell -> i + 2
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

        # return dfs(0, True)

        #################### solution 2 ##############################
        buy = float('-inf')   # holding stock
        sell = 0              # just sold today
        cooldown = 0          # resting / cooldown finished

        for price in prices:
            prev_sell = sell

            sell = buy + price
            buy = max(buy, cooldown - price)
            cooldown = max(cooldown, prev_sell)

        return max(sell, cooldown)
