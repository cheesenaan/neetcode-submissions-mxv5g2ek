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

            max_left = max(dfs(root.left), 0)
            max_right = max(dfs(root.right), 0)
            
            # update gloabl res
            res = max(res, max_left + max_right + root.val)

            # retune max child up
            return root.val + max(max_left, max_right, 0)

        dfs(root)
        return res
        