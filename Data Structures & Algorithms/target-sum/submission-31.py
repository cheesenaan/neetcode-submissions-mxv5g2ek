class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        
        def dfs(total, i):
            if i == len(nums):
                return 1 if total == target else 0

            return dfs(total + nums[i], i+1) + dfs(total - nums[i], i+1)

        return dfs(0,0)
        