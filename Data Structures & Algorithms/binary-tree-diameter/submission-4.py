# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        res = 0

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)
            d = left + right
            res = max(res, d)
            h = 1 + max(left, right)
            print("node : ", node.val, "diameter : ", d, "height : ", h)
            return h

        dfs(root)
        return res