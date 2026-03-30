class Solution:
    # Time Complexity: O(n * 2^n)
    #   - There are 2^n subsets
    #   - Copying each subset takes O(n)
    #
    # Space Complexity: O(n)
    #   - Recursion depth up to n
    #   - Output space is not counted

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()          # sort to group duplicates
        res, cur = [], []

        def dfs(i):
            # If we've considered all elements, record the subset
            if i == len(nums):
                res.append(cur[:])
                return

            # --------------------
            # Choice 1: include nums[i]
            # --------------------
            cur.append(nums[i])
            dfs(i + 1)
            cur.pop()

            # --------------------
            # Choice 2: exclude nums[i]
            # Skip all duplicates of nums[i]
            # --------------------
            while i < len(nums) - 1 and nums[i] == nums[i + 1]:
                i += 1

            dfs(i + 1)

        dfs(0)
        return res
