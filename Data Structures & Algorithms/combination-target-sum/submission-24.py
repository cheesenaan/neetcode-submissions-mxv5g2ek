class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # res will store all valid combinations
        # cur keeps track of the current combination being built
        res, cur = [], []

        def dfs(total, i):
            """
            total: current sum of elements in cur
            i: current index in nums we are considering
            """

            # If current sum equals target, we found a valid combination
            if total == target:
                # Append a copy of cur since cur will change later
                res.append(cur[:])
                return

            # If sum exceeds target OR we've used all numbers, stop exploring this path
            if total > target or i == len(nums):
                return 

            # --------------------
            # Choice 1: INCLUDE nums[i]
            # --------------------
            # Add nums[i] to the current combination
            cur.append(nums[i])

            # Recurse with updated sum
            # We pass i again (not i + 1) because we can reuse the same number
            dfs(total + nums[i], i)

            # Backtrack: remove the last added number
            cur.pop()

            # --------------------
            # Choice 2: EXCLUDE nums[i]
            # --------------------
            # Move to the next index
            dfs(total, i + 1)

        # Start DFS with sum = 0 and index = 0
        dfs(0, 0)

        return res
