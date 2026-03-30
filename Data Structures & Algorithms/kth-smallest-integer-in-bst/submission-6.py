# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        # pre order traversal
        res = None

        def dfs(node):
            nonlocal res,k 

            if not node:
                return node

            dfs(node.left)
            k = k - 1
            if k == 0:
                res = node.val
                return
            dfs(node.right)

        
        dfs(root)
        return res


            



        

        