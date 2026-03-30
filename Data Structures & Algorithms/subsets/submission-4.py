class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def backtracking(i):
            if i == len(nums):
                return res.append(subset[:])

            # include number
            subset.append(nums[i])
            backtracking(i+1)

            # exclude number
            subset.pop()
            backtracking(i+1)

        backtracking(0)
        return res


