class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        
        hp = {}
        def dfs(total, i):
            if total == target:
                return True

            if total > target or i == len(nums):
                return False

            if (total, i) in hp:
                return hp[(total, i)]

            hp[(total, i)] = dfs(total, i+1) or dfs(total + nums[i], i+1)
            return hp[(total, i)]

        return dfs(0,0)
        

        
        