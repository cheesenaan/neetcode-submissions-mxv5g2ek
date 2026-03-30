class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res, cur = [], []

        def dfs(total, i):
            if total == target:
                return res.append(cur[:])

            if total > target or i == len(nums):
                return 

            # current nums[i] unlimited number of times
            cur.append(nums[i])
            dfs(total + nums[i], i)
            cur.pop()
            # skip nums[i] 
            dfs(total, i+1)

        dfs(0,0)
        return res



        