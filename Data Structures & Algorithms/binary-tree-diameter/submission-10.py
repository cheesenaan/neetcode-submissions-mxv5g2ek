# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        d = 0

        # return height
        def dfs(node):
            nonlocal d

            if not node:
                return 0

            left, right = dfs(node.left), dfs(node.right)
            d = max(d, left+right)
            h = 1 + max(left, right)
            return h

        dfs(root)
        return d

        