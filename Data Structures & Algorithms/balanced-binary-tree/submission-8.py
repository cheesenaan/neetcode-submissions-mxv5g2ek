import math
from typing import Optional

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # recursive dfs
        # O(n) time and O(h) space
        
        # def dfs(node):
        #     if not node:
        #         return 0

        #     left = dfs(node.left)
        #     if left == -1:
        #         return -1

        #     right = dfs(node.right)
        #     if right == -1:
        #         return -1

        #     if not (0 <= abs(left - right) <= 1):
        #         return -1

        #     return 1 + max(left, right)

        # return dfs(root) != -1

        if not root:
            return True

        stack = [[root, False]]
        h = {} # node address : height

        while stack:
            node , v = stack.pop()

            if v:
                left_h = h.get(node.left, 0)
                right_h = h.get(node.right, 0)
                if not (0 <= abs(left_h - right_h) <= 1):
                    return False
                h[node] = 1 + max(left_h, right_h)
            else:
                stack.append([node, True])

                if node.right:
                    stack.append([node.right, False])

                if node.left:
                    stack.append([node.left, False])

        return True



        