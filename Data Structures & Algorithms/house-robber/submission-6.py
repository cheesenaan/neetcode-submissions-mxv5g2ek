class Solution:
    def rob(self, nums: List[int]) -> int:

        # memo = [-1] * len(nums)
        
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0

        #     if memo[i] != -1:
        #         return memo[i]

        #     return max(dfs(i+1), nums[i] + dfs(i+2))

        # return dfs(0)

        # [rob1, rob2, n, n+1, ...]
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2


        