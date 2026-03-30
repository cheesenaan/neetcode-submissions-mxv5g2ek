class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums:
            return []
        
        res, cur = [], []

        def dfs(i):
            if i == len(nums):
                return res.append(cur[:])

            # include
            cur.append(nums[i])
            dfs(i+1)

            cur.pop()
            dfs(i+1)

        dfs(0)
        return res
        