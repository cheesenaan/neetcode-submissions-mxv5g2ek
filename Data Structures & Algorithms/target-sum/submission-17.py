class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = (sum(nums) + target) // 2

        if total < 0 or (sum(nums) + target) % 2:
            return 0

        dp = [0] * (total+1)
        dp[0] = 1
        for num in nums:
            for j in range(total, num-1, -1):
                dp[j] += dp[j-num]

        return dp[total]

        
        