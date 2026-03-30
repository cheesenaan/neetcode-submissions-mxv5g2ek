class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []

        def dfs(i):
            if i == len(nums):
                return res.append(nums[:])

            for j in range(i, len(nums)):
                # swap
                nums[i], nums[j] = nums[j], nums[i]
                dfs(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        dfs(0)
        return res



        