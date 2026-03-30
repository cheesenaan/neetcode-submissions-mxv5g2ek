class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # dp[i] = max length subsequence that ends at index i

        dp = [1] * (len(nums))

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp)

        