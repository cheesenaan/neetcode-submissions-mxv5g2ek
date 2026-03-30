class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        cur, res = [], []

        def dfs(i):
            if i == len(nums):
                return res.append(cur[:])

            # include
            cur.append(nums[i])
            # Decision made → move forward
            dfs(i+1)
            # exclude
            cur.pop()
            # Decision made → move forward
            dfs(i+1)


        dfs(0)
        return res
        