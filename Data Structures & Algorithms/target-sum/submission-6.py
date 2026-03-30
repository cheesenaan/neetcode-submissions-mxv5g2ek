class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        ################### SOLUTION 1 ###################
        # time = O(n*m) where n = len(nums), m = sum(nums)
        # space = O(n*m) where n = len(nums), m = sum(nums)
        # memo = {} # (total, i) -> count
        # def dfs(total, i):
        #     # base case : used all numbers
        #     if i == len(nums):
        #         return 1 if total == target else 0

        #     if (total, i) in memo:
        #         return memo[(total, i)]

        #     memo[(total, i)] = dfs(total + nums[i], i+1) + dfs(total - nums[i], i+1)

        #     return memo[(total, i)]

        # return dfs(0, 0)

        ################### SOLUTION 2 ###################

        total_sum = sum(nums)

        # If target impossible
        if total_sum < abs(target) or (total_sum + target) % 2 != 0:
            return 0

        subset_sum = (total_sum + target) // 2

        # dp[i] = # of ways to reach sum i
        dp = [0] * (subset_sum + 1)
        dp[0] = 1  # 1 way to make sum 0

        for num in nums:
            # iterate backwards to avoid overwriting previous results
            for s in range(subset_sum, num - 1, -1):
                dp[s] += dp[s - num]

        return dp[subset_sum]


            