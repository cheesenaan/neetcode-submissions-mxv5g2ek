# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # in order traversal

        res = None

        def inOrderDfs(node):
            nonlocal k, res
            if not node:
                return node

            inOrderDfs(node.left)

            k = k - 1
            if k == 0:
                res = node.val
                return
            
            inOrderDfs(node.right)

        inOrderDfs(root)
        return res