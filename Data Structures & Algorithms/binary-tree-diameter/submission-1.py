# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        diamter = self.maxHeight(root.left) + self.maxHeight(root.right)

        print("node : " , root.val, " diamter : ", diamter)
        maxD = max(diamter, self.diameterOfBinaryTree(root.left),  self.diameterOfBinaryTree(root.right))
        return max(diamter, maxD)


    def maxHeight(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0

        return 1 + max(self.maxHeight(node.left), self.maxHeight(node.right))



        