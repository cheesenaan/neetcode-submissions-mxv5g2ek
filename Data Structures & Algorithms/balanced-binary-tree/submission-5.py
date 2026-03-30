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

        # post order traversal, bottom up, using height in stack
        # def dfs(node):
        #     if not node:
        #         return 0

        #     left_h = dfs(node.left)
        #     if left_h == -1:
        #         return -1

        #     right_h = dfs(node.right)
        #     if right_h == -1:
        #         return -1

        #     if abs(left_h - right_h) > 1:
        #         return -1

        #     return 1 + max(left_h, right_h)

        # return dfs(root) != -1

        # iterative dfs - stack

        if not root:
            return True

        stack = [[root, False]]
        h = {} # node address : height of node

        while stack:
            node , v = stack.pop()

            if v:
                left_h = h.get(node.left, 0)
                right_h = h.get(node.right, 0)
                if abs(right_h - left_h) > 1:
                    return False
                h[node] = 1 + max(left_h, right_h)

            else:
                stack.append([node, True])
                if node.right:
                    stack.append([node.right, False])
                if node.left:
                    stack.append([node.left, False])

        return True




        