# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        res = root.val

        def dfs(node):
            nonlocal res

            if not node:
                return 0

            maxLeft = max(dfs(node.left), 0)
            maxRight = max(dfs(node.right), 0)

            # compute max - with both children
            res = max(res, maxLeft + maxRight + node.val )

            # return node with only max child
            return node.val + max(maxLeft, maxRight)


        dfs(root)
        return res

        