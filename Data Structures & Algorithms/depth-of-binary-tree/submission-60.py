# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        res = 0
        def dfs(root):
            nonlocal res

            if not root:
                return 0

            left_h = dfs(root.left)
            right_h = dfs(root.right)
            h = max(left_h, right_h) + 1
            res = max(res, h)
            return h

        dfs(root)
        return res
            


            


        