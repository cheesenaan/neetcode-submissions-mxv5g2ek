class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:


        res, cur = [], []

        def dfs(total, i):
            if total == target:
                return res.append(cur[:])

            if total > target or i == len(nums):
                return 
            
            # include same
            cur.append(nums[i])
            dfs(nums[i] + total, i)

            # skip
            cur.pop()
            dfs(total, i+1)

        dfs(0,0)
        return res

        
       