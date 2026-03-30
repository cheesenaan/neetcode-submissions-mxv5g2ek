# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        maxD = 0

        def dfs(node):
            nonlocal maxD

            if not root:
                return 0

            left_h = dfs(node.left) if node.left else 0
            right_h = dfs(node.right) if node.right else 0

            maxD = max(maxD, left_h + right_h)
            return 1 + max(left_h, right_h)

        
        dfs(root)
        return maxD

