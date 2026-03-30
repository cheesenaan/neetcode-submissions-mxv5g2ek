# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # recursive dfs - O(n) time and O(h) space - o(nlogn) best case, o(n) worst case
        
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        # iterative dfs - stack
        # pre order traversal, bottom up, children processed first
        maxDepth = 0

        def dfs(node):
            if not node:
                return 0

            left_h = dfs(node.left)
            right_h = dfs(node.right)
            maxDepth = max(maxDepth, left_h + right_h)
            return 1 + max(left_h, right_h)

        return maxDepth

            

        

        
        