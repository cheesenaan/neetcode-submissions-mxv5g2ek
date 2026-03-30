class Solution:
    def rob(self, nums: List[int]) -> int:

        # def dfs(i):
        #     if i == len(nums):
        #         return 1
            
        #     if i == len(nums):
        #         return 0

        #     return max(nums[i]+dfs(i+2), dfs(1))

        # return dfs(0)

        # [rob1, rob2, n , n + 1, ...]
        rob1, rob2 = 0 ,0
        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2

        