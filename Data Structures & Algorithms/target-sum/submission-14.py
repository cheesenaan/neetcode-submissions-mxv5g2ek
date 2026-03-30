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

        # time = O(n*m) where n = len(nums), m = sum(nums)
        # space = O(m) where n = len(nums), m = sum(nums)

        # Step 1: Transform the Target Sum problem into a subset sum problem
        # total = sum of subset P where numbers are assigned '+'
        # sum(P) = (sum(nums) + target) / 2
        total = (sum(nums) + target) // 2

        # Step 2: Check for impossible cases
        # Case 1: total < 0 → cannot have negative subset sum
        # Case 2: (sum(nums) + target) % 2 != 0 → total is not an integer, impossible
        if total < 0 or (sum(nums) + target) % 2 != 0:
            return 0

        # Step 3: Initialize DP array
        # dp[i] = number of ways to get sum i using a subset of nums
        dp = [0] * (total + 1)
        dp[0] = 1  # Base case: there is 1 way to make sum 0 (use empty subset)

        # Step 4: Fill DP array
        for n in nums:
            # Iterate backwards to prevent using the same number multiple times
            for j in range(total, n - 1, -1):
                # For sum j, add ways of forming sum j-n
                dp[j] += dp[j - n]

        # Step 5: The answer is the number of ways to make subset sum = total
        return dp[total]