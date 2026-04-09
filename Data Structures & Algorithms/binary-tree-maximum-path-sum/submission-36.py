# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        res = -float('inf')
        def dfs(node):
            nonlocal res
            # base case
            if not node:
                return 0

            left_max = max(dfs(node.left), 0)
            right_max = max(dfs(node.right), 0)
            res = max(res, left_max + right_max + node.val)
            return node.val + max(left_max, right_max)

        dfs(root)
        return res
