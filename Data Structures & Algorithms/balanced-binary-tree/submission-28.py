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


        def dfs(node):
            if not node:
                return 0

            left_h = dfs(node.left)
            if left_h == -1:
                return -1

            right_h = dfs(node.right)
            if right_h == -1:
                return -1

            if not (0 <= abs(left_h-right_h) <= 1):
                return -1

            return 1 + max(left_h, right_h)

        return dfs(root) != -1

        def dfs_iterative(node):
            q = deque()
            q.append([node, False])
            hp = {}
            while q:
                cur, v = q.popleft()
                if v:
                    left_h = hp.get(cur.left, 0)
                    right_h = hp.get(cur.right, 0)
                    if not (0 <= abs(left_h-right_h) <= 1):
                        return False
                    hp[cur] = 1 + max(left_h, right_h)
                else:
                    q.append([cur, True])
                    if cur.left:
                        q.append([cur.left, False])
                    if cur.right:
                        q.append([cur.right, False])
            return True
        
        return dfs_iterative(root)


        