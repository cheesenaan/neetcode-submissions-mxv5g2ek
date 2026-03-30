class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2:
            return False

        target = sum(nums) // 2

        def dfs(total, i):
            if total == target:
                return True

            if total > target or i == len(nums):
                return False

            return dfs(total, i+1) or dfs(total + nums[i], i+1)


        return dfs(0,0)
        

        
        