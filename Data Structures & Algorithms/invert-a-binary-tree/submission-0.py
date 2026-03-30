# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node):
            if node == None:
                return

            if node.left == None and node.right == None:
                return 

            l = node.left if node.left else None
            r = node.right if node.right else None
            node.left = r
            node.right = l

            invert(node.left)
            invert(node.right)

        invert(root)
        return root





        