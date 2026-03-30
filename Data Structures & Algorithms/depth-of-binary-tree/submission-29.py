# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        
        # recursive - dfs
        # O(n) time, O(h) space

        # if not root:
        #     return 0


        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        # iterative dfs 

        if not root:
            return 0

        stack = [[root, 1]]
        maxDepth = 0

        while stack:
            node, level = stack.pop()

            maxDepth = max(maxDepth, level)

            if node.left:
                stack.append([node.left, level+1])

            if node.right:
                stack.append([node.right, level+1])


        return maxDepth




        