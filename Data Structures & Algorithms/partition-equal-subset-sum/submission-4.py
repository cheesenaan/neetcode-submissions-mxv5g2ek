class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # if total if odd, partition cant be equal 
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        dp = [False] * (target+1)
        dp[0] = True

        for num in nums:
            for j in range(target, num-1, -1):
                dp[j] = dp[j] or dp[j-num]
        
        return dp[target]
        
        # memo = {}
        # def dfs(i, total):
        #     if total == target:
        #         return True

        #     if total > target or i == len(nums):
        #         return False

        #     if (i, total) in memo:
        #         return memo[(i, total)]

        #     # skip or add
        #     res =  dfs(i+1, total) or dfs(i+1, total+nums[i])
        #     memo[i] = [(i, total)]

        #     return res

        
        # return dfs(0,0)





        