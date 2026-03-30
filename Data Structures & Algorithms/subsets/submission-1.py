class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:


        res = []
        subset = []

        def backtracking(index):

            if index == len(nums):
                return res.append(subset[:])

            # include index
            subset.append(nums[index])
            backtracking(index + 1)

            # exclude
            subset.pop()
            backtracking(index + 1)

        
        backtracking(0)
        return res


