class Solution:
    def rob(self, nums: List[int]) -> int:

        # backtrack o(2^n) time and o(n) space

        # def dfs(i):
        #     if i >= len(nums):
        #         return 0

        #     return max(dfs(i+1), nums[i]+dfs(i+2))

        # return dfs(0)

        # o(n) time and space
        # arr = [-1] * len(nums)
        # def dfs(i):
        #     if i >= len(nums):
        #         return 0
        #     if arr[i] != -1:
        #         return arr[i]
        #     return max(dfs(i+1), nums[i]+dfs(i+2))

        # return dfs(0)

        #[rob1, rob2, n, n+1 ... ]
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob1+n, rob2)
            rob1 = rob2
            rob2 = temp
        
        return rob2
