class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        # dp[i] = T, F if can  the array into two subsets equal to i 
        dp = [False] * (target+1)
        dp[0] = True

        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i]]

        return dp[target]
