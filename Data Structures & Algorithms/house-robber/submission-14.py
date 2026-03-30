class Solution:
    def rob(self, nums: List[int]) -> int:

        # dp[i] = max money for first i houses 

        n = len(nums)

        if n == 0:
            return 0
        if n == 1:
            return nums[0]


        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = nums[0]

        for i in range(2, n+1):
            dp[i] = max(
                dp[i-1], # skip
                dp[i-2] + nums[i-1] #rob
            )

        print(dp)
        return dp[n]

       
        