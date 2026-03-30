class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        curr = []
        
        def dfs(i, curr, total):
            if total == target:
                res.append(curr[:])
                return
            if i >= len(nums) or total > target:
                return

            # include current
            curr.append(nums[i])
            dfs(i, curr, total + nums[i])

            # exclude current and skip to next
            curr.pop()
            dfs(i+1, curr, total)

        dfs(0, curr, 0)
        return res


            

       