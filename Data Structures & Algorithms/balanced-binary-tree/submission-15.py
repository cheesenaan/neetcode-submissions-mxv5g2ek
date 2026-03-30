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


        # recusrive
        # def dfs(node):
        #     if not node:
        #         return 0

        #     left_h = dfs(node.left)
        #     if left_h == -1:
        #         return -1

        #     right_h = dfs(node.right)
        #     if right_h == -1:
        #         return -1

        #     if not (0 <= abs(left_h-right_h) <=1):
        #         return -1

        #     return 1 + max(left_h, right_h)

        
        # return dfs(root) != -1

        # bfs
        if not root:
            return True
        hp = {}
        stack = [[root, False]]

        while stack:
            node, v = stack.pop()
            if v:
                left_h = hp.get(node.left, 0)
                right_h = hp.get(node.right, 0)
                if not (0 <= abs(left_h - right_h) <= 1):
                    return False
                hp[node] = 1 + max(left_h,right_h)
            else:
                stack.append([node, True])
                if node.left:
                    stack.append([node.left, False])
                if node.right:
                    stack.append([node.right, False])

        return True

