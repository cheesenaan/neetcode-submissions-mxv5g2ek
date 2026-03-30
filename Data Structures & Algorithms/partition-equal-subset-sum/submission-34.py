class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # if odd then false
        if sum(nums) % 2 != 0:
            return False

        total = sum(nums) // 2
        dp = [False] * (total+1)
        dp[0] = True

        for n in nums:
            for j in range(total, n-1, -1):
                dp[j] = dp[j] or dp[j-n]

        return dp[total]