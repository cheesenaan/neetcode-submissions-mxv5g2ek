# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:


        # recusrive dfs
        
        # def dfs(left, root, right):

        #     if not root:
        #         return True

        #     if not (left < root.val < right):
        #         return False

        #     return dfs(left, root.left, root.val) and dfs(root.val, root.right, right)



        # return dfs(-float('inf'), root, float('inf'))


        # iterative dfs

        if not root:
                return True

        stack = [[-float('inf'), root, float('inf')]]

        while stack:
            left, root, right = stack.pop()

            if not (left < root.val < right):
                return False

            if root.left:
                stack.append([left, root.left, root.val])

            if root.right:
                stack.append([root.val, root.right, right])

        return True



