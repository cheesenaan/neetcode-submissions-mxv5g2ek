class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        
        # dp = {}
        # def dfs(total, i):
        #     if i == len(nums):
        #         return 1 if total == target else 0

        #     if (total, i) in dp:
        #         return dp[(total, i)]

        #     dp[(total, i)] = dfs(total + nums[i], i+1) + dfs(total - nums[i], i+1)
        #     return dp[(total, i)] 
        
        # return dfs(0,0)

        total = (sum(nums) + target) // 2

        if total < 0 or (sum(nums) + target) % 2 != 0:  # ensure integer subset
            return 0

        dp = [0] * (total+1)
        dp[0] = 1
        for n in nums:
            # prevent dups
            for j in range(total, n-1, -1):
                dp[j] += dp[j-n]

        return dp[total]


