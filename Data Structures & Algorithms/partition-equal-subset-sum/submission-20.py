class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # If total sum is odd, it cannot be split into two equal subsets
        if sum(nums) % 2:
            return False

        # Target sum for one subset (half of total sum)
        target = sum(nums) // 2

        # dp[j] will be True if we can form a subset with sum = j
        dp = [False] * (target + 1)

        # Base case: sum 0 is always achievable (choose no elements)
        dp[0] = True

        # Iterate through each number in the array
        for num in nums:

            # Traverse backwards to avoid reusing the same number multiple times
            for j in range(target, num - 1, -1):

                # dp[j] becomes True if:
                # 1) dp[j] was already True (we don't use num), OR
                # 2) dp[j - num] was True (we use num)
                dp[j] = dp[j] or dp[j - num]

        # If we can form a subset with sum == target,
        # the remaining numbers also form a subset with sum == target
        return dp[target]
