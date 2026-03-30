# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        
        self.res = float('-inf')

        def dfs(node):

            if not node:
                return 0

            maxLeft = max(dfs(node.left), 0)
            maxRight = max(dfs(node.right), 0)

            # update global res
            self.res = max(self.res, maxLeft + maxRight + node.val)

            # return max path up
            return node.val + max(maxLeft, maxRight, 0)

        dfs(root)
        return self.res


            

       
        