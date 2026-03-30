class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        

        res, cur = [], []

        def backtrack(total, i):
            if total == target:
                return res.append(cur[:])

            if total > target or i >= len(nums):
                return

            # current unlimited number of times
            cur.append(nums[i])
            backtrack(total + nums[i], i)
            cur.pop()
            backtrack(total, i+1)

        backtrack(0,0)
        return res
        