# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        def findDepth(node):
            if not node:
                return 0
            return 1  + max(findDepth(node.left), findDepth(node.right))

        stack = [root]
        while stack:
            node = stack.pop()
            leftD = findDepth(node.left)
            rightD = findDepth(node.right)

            if (math.fabs(rightD - leftD) > 1) :
                return False

            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return True

        