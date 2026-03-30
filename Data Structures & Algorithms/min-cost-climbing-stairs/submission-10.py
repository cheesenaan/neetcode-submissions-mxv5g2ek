class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        # brute force
        memo = {}
        def dfs(i):
            if i >= len(cost):
                return 0

            if i in memo:
                return memo[i]

            return cost[i] + min(dfs(i+1), dfs(i+2))

        return min(dfs(0), dfs(1))
        