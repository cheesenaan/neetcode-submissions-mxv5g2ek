# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inOrderDfs(node):
            nonlocal k, res

            if not node:
                return 0

            inOrderDfs(node.left)

            k = k - 1
            if k == 0:
                res  = node.val
                return 
            

            inOrderDfs(node.right)

        res = None
        inOrderDfs(root)
        return res

            