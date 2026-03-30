# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = -float('inf')

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            left_h = max(dfs(root.left), 0)
            right_h = max(dfs(root.right), 0)

            # global
            res = max(res, root.val + left_h + right_h)

            # return max child up
            return root.val + max(left_h, right_h, 0)

        dfs(root)
        return res
        