# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        if not root:
            return root
        
        minV = float('inf')

        def dfs(node):
            nonlocal k, minV

            if not node:
                return 

            dfs(node.left)
            k -= 1
            if k == 0:
                minV = node.val
                return node.val
            dfs(node.right)

        dfs(root)
        return minV
        
        
        # if not root:
        #     return root

        # curr = root
        # stack = []

        # while stack or curr:
        #     while curr:
        #         stack.append(curr)
        #         curr = curr.left
        #     curr = stack.pop()
        #     k -= 1
        #     if k == 0:
        #         return curr.val
        #     curr = curr.right
