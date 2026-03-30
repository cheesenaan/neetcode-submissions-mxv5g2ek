class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def backtracking(i):
            if len(nums) == i:
                return res.append(subset[:])

            # include
            subset.append(nums[i])
            backtracking(i+1)

            #exclude
            subset.pop()
            backtracking(i+1)

        backtracking(0)
        return res
        
