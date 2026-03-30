class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # dp[i] = max subsequence length at index i for nums[:i]

        dp = [1] * (len(nums)+1) # every element is subsequence of itself

        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)

        return max(dp) 


        