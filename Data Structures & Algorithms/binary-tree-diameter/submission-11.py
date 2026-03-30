# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        
        # recursive dfs
        
        # d = 0

        # # return height
        # def dfs(node):
        #     nonlocal d

        #     if not node:
        #         return 0

        #     left, right = dfs(node.left), dfs(node.right)
        #     d = max(d, left+right)
        #     h = 1 + max(left, right)
        #     return h

        # dfs(root)
        # return d

        #O(n) time where n is the number of nodes in tree
        # O(h) space where h is the height of the tree. O(nlogn) best case, O(n) worst case

        # iterative dfs - stack
        stack = [[root, False]]
        h = {} # node address : height
        d = 0

        while stack:
            node, v = stack.pop()

            if v:
                left_h = h.get(node.left, 0)
                right_h = h.get(node.right, 0)
                d = max(d, left_h + right_h)
                h[node] = 1 + max(left_h, right_h)
            else:
                stack.append([node, True])
                if node.left:
                    stack.append([node.left, False])
                if node.right:
                    stack.append([node.right, False])

        return d




        