# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        maxDepth = 0

        def dfs(node):
            nonlocal maxDepth

            if not node:
                return 0

            left_h = dfs(node.left)
            right_h = dfs(node.right)

            h = 1 + max(left_h, right_h)
            maxDepth = max(maxDepth, h)

            return h

        return dfs(root)

            


        