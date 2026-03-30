# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # recursive dfs

        # if root is None:
        #     return root

        # if root.left is None and root.right is None:
        #     return root

        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)
        
        # return root

        # iterative dfs with stack (first in last out)
        if root is None:
            return root

        stack = [root]

        while stack:
            node = stack.pop()

            node.left, node.right = node.right, node.left

            if node.left:
                stack.append(node.left)

            if node.right:
                stack.append(node.right)

        return root


        

