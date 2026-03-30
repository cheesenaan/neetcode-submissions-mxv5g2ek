class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        res = []
        comb = []

        def dfs(total, i):
            if total == target:
                return res.append(comb[:])

            if i == len(nums) or total > target:
                return None

            # current
            comb.append(nums[i])
            dfs(total + nums[i], i)

            # skip current
            comb.pop()
            dfs(total, i+1)

        dfs(0, 0)
        return res
