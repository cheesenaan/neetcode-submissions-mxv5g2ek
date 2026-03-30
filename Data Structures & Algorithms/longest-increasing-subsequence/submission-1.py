class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # dp[i] = max subsequence length at i for nums[:i]
        n = len(nums)
        dp = [1] * n # every element is a subsequence of length 1

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)