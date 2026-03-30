# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        d = 0

        def dfs(node):
            nonlocal d

            if not node:
                return 0

            left_h = dfs(node.left)
            right_h = dfs(node.right)

            d = max(d, left_h + right_h)
            h = 1 + max(left_h, right_h)
            return h

        dfs(root)
        return d



       
        