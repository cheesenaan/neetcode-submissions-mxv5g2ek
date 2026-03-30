class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        # time = O(n∗m)
        # space = O(n∗m)
        memo = {} # (total, i) -> count
        def dfs(total, i):
            # base case : used all numbers
            if i == len(nums):
                return 1 if total == target else 0

            if (total, i) in memo:
                return memo[(total, i)]

            memo[(total, i)] = dfs(total + nums[i], i+1) + dfs(total - nums[i], i+1)

            return memo[(total, i)]

        return dfs(0, 0)


            