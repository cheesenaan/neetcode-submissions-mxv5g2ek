# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        max_so_far = 0
        def dfs(node):
            nonlocal k, max_so_far

            if not node:
                return 

            dfs(node.left)
            k -= 1
            if k == 0:
                max_so_far = node.val
                return
            dfs(node.right)    

        dfs(root)
        return max_so_far