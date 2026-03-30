class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        # If total sum is odd, it cannot be split into two equal subsets
        if sum(nums) % 2:
            return False

        # Target sum for one subset
        target = sum(nums) // 2

        # dp[j] = True if we can form sum j using some subset of nums
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum 0 is always achievable (empty subset)

        # Iterate through each number
        for num in nums:
            # Traverse backwards to avoid reusing the same number multiple times
            for j in range(target, num - 1, -1):
                # Either we already could form j,
                # or we can form j by adding current num to (j - num)
                dp[j] = dp[j] or dp[j - num]

        # If we can form target, the rest also sums to target
        return dp[target]
