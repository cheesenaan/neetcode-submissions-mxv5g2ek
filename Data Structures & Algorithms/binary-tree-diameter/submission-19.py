# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # d = 0

        # def dfs(node):
        #     nonlocal d

        #     if not node:
        #         return 0

        #     left_h = dfs(node.left)
        #     right_h = dfs(node.right)

        #     d = max(d, left_h + right_h)
        #     h = 1 + max(left_h, right_h)
        #     return h

        # dfs(root)
        # return d

        if not root:
            return 0

        d = 0
        h = {} # node address : height
        stack = [[root, False]]

        while stack:
            node, v = stack.pop()

            if v:
                left_h = h.get(node.left, 0)
                right_h = h.get(node.right, 0)
                d = max(d, left_h + right_h)
                h[node] = 1 + max(left_h, right_h)
            else:
                stack.append([node, True])

                if node.right:
                    stack.append([node.right, False])

                if node.left:
                    stack.append([node.left, False])

        return d






       
        