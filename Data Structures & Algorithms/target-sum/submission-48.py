class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        hp = {}
        def dfs(total, i):
            if i == len(nums):
                return 1 if total == target else 0

            if (total, i) in hp:
                return hp[(total, i)]

            hp[(total, i)] =  dfs(nums[i] + total, i+1) + dfs(total - nums[i], i+1) 
            return hp[(total, i)]

        return dfs(0,0)
