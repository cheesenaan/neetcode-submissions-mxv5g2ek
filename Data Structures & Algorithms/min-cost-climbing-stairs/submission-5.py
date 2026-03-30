class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # brute force o(2^n) time and o(1) space
        def dfs(i):
            if i >= len(cost):
                return 0
            return cost[i] + min(dfs(i+1), dfs(i+2))

        return min(dfs(0), dfs(1))
        