class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

       ################### SOLUTION 3 ###################
        # DP where the key is the current sum
        # dp[sum] = number of ways to reach this sum using processed numbers

        from collections import defaultdict

        dp = defaultdict(int)
        dp[0] = 1
        # Base case:
        # There is exactly 1 way to reach sum = 0 before using any numbers
        # (by choosing nothing)

        for n in nums:
            # next_dp will store counts after processing current number n
            next_dp = defaultdict(int)

            for total, count in dp.items():
                # Option 1: add current number
                # If we previously had `count` ways to reach `total`,
                # then we now have `count` ways to reach (total + n)
                next_dp[total + n] += count

                # Option 2: subtract current number
                # Similarly, `count` ways to reach (total - n)
                next_dp[total - n] += count

            # Move to the next iteration
            # dp now represents all sums achievable after processing this number
            dp = next_dp

        # The answer is the number of ways to reach `target`
        return dp[target]

