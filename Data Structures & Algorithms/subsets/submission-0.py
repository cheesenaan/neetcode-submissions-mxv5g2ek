class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        res = []
        subset = []

        def backtracking(index):

            if index == len(nums):
                res.append(subset[:])
                return 

            # include value
            subset.append(nums[index])
            backtracking(index + 1)

            # exclude value
            subset.pop()
            backtracking(index + 1)

        backtracking(0)
        return res
