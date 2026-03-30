class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        # if len(nums) == 0:
        #     return [[]]

        # res = []

        # perms = self.permute(nums[1:])
        # for perm in perms:
        #     for i in range(len(perm)+1):
        #         p_copy = perm.copy()
        #         p_copy.insert(i, nums[0])
        #         res.append(p_copy)

        # return res

        res = []
        def backtracking(i):
            if i == len(nums):
                return res.append(nums[:])

            for j in range(i, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                backtracking(i+1)
                nums[i], nums[j] = nums[j], nums[i]

        backtracking(0)
        return res



        

        