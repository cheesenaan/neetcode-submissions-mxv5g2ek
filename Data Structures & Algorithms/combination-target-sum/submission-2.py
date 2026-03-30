class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        res = []
        comb = []

        def dfs(comb, total, i):
            if total == target:
                return res.append(comb[:])

            if i == len(nums) or total > target:
                return None

            # current
            comb.append(nums[i])
            dfs(comb, total + nums[i], i)

            # skip current
            comb.pop()
            dfs(comb, total, i+1)

        dfs(comb, 0, 0)
        return res
