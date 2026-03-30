# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        #o(n) time and o(n) space
        res = -float('inf')
        def dfs(node):
            nonlocal res
            if not node:
                return 0

            max_left = max(dfs(node.left), 0)
            max_right = max(dfs(node.right), 0)

            # update gloab
            res = max(res, max_left + max_right + node.val )

            # return max up
            return node.val + max(max_left, max_right, 0)
        
        dfs(root)
        return res



        
        