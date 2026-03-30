class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # dp[i] = length of the longest increasing subsequence that ENDS at index i
        n = len(nums)
        dp = [1] * n  # every element is a subsequence of length 1

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    # Among all previous elements smaller than nums[i],
                    # pick the one with the longest LIS, and extend it by 1
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
