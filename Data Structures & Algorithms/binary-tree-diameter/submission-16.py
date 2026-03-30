# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

       
        # post order traversal 
        
        # recursive dfs
        # O(n) time and O(h) space
        
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

        # iterative dfs

        if not root:
            return 0

        stack = [[root, False]]
        d = 0
        h = {} # node address : height

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



        


        
        