class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # time = O(n*m) where n = len(nums), m = sum(nums)
        # space = O(n*m) where n = len(nums), m = sum(nums)
        # dp = {}
        # def dfs(total, i):
        #     if i == len(nums):
        #         return 1 if total == target else 0

        #     if (total, i) in dp:
        #         return dp[(total, i)]

        #     dp[(total, i)] =  dfs(total + nums[i], i+1) + dfs(total - nums[i], i+1)
        #     return dp[(total, i)]

        # return dfs(0,0)

        # convert to subset problem
        total = (sum(nums) + target) // 2

        if total < 0 or (sum(nums) + target) % 2:
            return 0

        dp = [0] * (total+1)
        dp[0] = 1
        for num in nums:
            for j in range(total, num-1, -1):
                dp[j] += dp[j - num]

        return dp[total]

        
            
        
        