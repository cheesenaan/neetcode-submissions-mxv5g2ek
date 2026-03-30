class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # if total if odd, partition cant be equal 
        if sum(nums) % 2 != 0:
            return False

        target = sum(nums) // 2

        memo = {}
        def dfs(i, total):
            if total == target:
                return True

            if total > target or i == len(nums):
                return False

            if (i, total) in memo:
                return memo[i, total]

            memo[i] = [i, total]

            # skip or add
            return dfs(i+1, total) or dfs(i+1, total+nums[i])

        
        return dfs(0,0)

        