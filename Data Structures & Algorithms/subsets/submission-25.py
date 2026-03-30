class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        # dfs(i+1) is called twice because we are exploring two choices for the same element, 
        # and using dfs(i) would cause infinite recursion
        res, cur = [], []

        def dfs(i):
            if i == len(nums):
                return res.append(cur[:])

            # include current
            cur.append(nums[i])
            dfs(i+1)
            cur.pop()

            # skip current
            dfs(i+1)

        dfs(0)
        return res

        