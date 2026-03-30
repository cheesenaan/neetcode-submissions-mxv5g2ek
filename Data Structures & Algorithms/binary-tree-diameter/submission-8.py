# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # recursive dfs - bottom up O(n) time and O(h) space

        # d = 0

        # def dfs(node):
        #     nonlocal d

        #     if not node:
        #         return 0

        #     left = dfs(node.left)
        #     right = dfs(node.right)
        #     d = max(d, left + right)
        #     h = 1 + max(left, right)

        #     return h

        # dfs(root)
        # return d


        # iterative dfs - stack
        stack = [[root, False]]
        h = {} # node address: height
        d = 0

        while stack:
            node , visitied = stack.pop()

            if visitied:
                # post order processing
                left_h = h.get(node.left, 0)
                right_h = h.get(node.right, 0)
                h[node] = 1 + max(left_h, right_h)
                d = max(d, left_h + right_h)
            else:
                stack.append([node, True])
                if node.left:
                    stack.append([node.left, False])
                if node.right:
                    stack.append([node.right, False])

        return d