# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # o(n) time and space - recursive
        # maxDepth = -float('inf')
        # def dfs(node):
        #     nonlocal maxDepth
        #     if not node:
        #         return 0

        #     left_h = dfs(node.left)
        #     right_h = dfs(node.right)
        #     maxDepth = max(maxDepth, left_h + right_h)
        #     return 1 + max(left_h, right_h)

        # return dfs(root)

        # o(n) time and space - dfs
        if not root:
            return 0
        stack = []
        stack.append((root, 1))
        maxDepth = -float('inf')
        while stack:
            node, depth = stack.pop()        
            maxDepth = max(maxDepth, depth)
            if node.left:
                stack.append((node.left, depth+1))
            if node.right:
                stack.append((node.right, depth+1))
        return maxDepth
        
