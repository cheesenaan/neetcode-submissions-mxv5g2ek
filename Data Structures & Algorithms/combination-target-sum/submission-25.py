class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        nums.sort()  # required for pruning
        res, cur = [], []

        def dfs(total, i):

            if total == target:
                res.append(cur[:])
                return

            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    break

                cur.append(nums[j])
                dfs(total + nums[j], j)
                cur.pop()

        # Start DFS with sum = 0 and index = 0
        dfs(0,0)

        return res
