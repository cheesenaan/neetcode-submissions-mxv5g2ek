class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:


        # brute force
        # memo = {}
        # def dfs(i):
        #     if i >= len(cost):
        #         return 0

        #     if i in memo:
        #         return memo[i]

        #     return cost[i] + min(dfs(i+1), dfs(i+2))

        # return min(dfs(0), dfs(1))

        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])


        return min(cost[0], cost[1])
        