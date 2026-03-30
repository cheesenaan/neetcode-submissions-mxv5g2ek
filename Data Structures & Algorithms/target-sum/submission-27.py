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

        #     return dfs(total + nums[i], i+1) + dfs(total - nums[i], i+1)

        
        # return dfs(0,0)

        total = (sum(nums) + target) // 2

        if total < 0 or (sum(nums) + target) % 2:
            return 0

        dp = [0] * (total+1)
        dp[0] = 1  # Base case: there is 1 way to make sum 0 (use empty subset)
        for num in nums:
            for j in range(total, num-1, -1):
                dp[j] += dp[j-num]

        return dp[total]

        