class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        # if odd then false
        if sum(nums) % 2 != 0:
            return False

        # check if one subarray can be met
        target = sum(nums) // 2
        hp = {}
        def dfs(total, i):
            if total == target:
                return True

            if total > target or i == len(nums):
                return False

            if (total, i) in hp:
                return hp[(total, i)]

            #keep number or skip number
            hp[(total, i)] = dfs(total, i+1) or dfs(total + nums[i], i+1)
            return hp[(total, i)]

        return dfs(0,0)
        