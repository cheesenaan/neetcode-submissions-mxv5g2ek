# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # O(n) time and space
        # def dfs(node):
        #     if not node:
        #         return 1

        #     left_h = dfs(node.left)
        #     if left_h == -1:
        #         return -1

        #     right_h = dfs(node.right)
        #     if right_h == -1:
        #         return -1

        #     if not (0 <= abs(left_h-right_h) <= 1):
        #         return -1

        #     return 1 + max(left_h, right_h)

        # return dfs(root) != -1

        if not root:
            return True
        stack = []
        stack.append((root, False))
        hp = {} # node : height
        while stack:
            node, v = stack.pop()
            if v:
                left_h = hp.get(node.left, 0)
                right_h = hp.get(node.right, 0)
                if not (0 <= abs(left_h-right_h) <= 1):
                    return False
                hp[node] = 1 + max(left_h, right_h)
            else:
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
                if node.right:
                    stack.append((node.right, False))

        return True

