class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res, cur = [], []

        def dfs(t, i):
            if t == target:
                return res.append(cur[:])

            if t > target or i == len(nums):
                return

            # include
            cur.append(nums[i])
            dfs(t + nums[i] , i )

            # exclude
            cur.pop()
            dfs(t , i +1)

        dfs(0,0)
        return res
