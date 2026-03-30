# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # recursive dfs - O(n) time and O(h) space - o(nlogn) best case, o(n) worst case
        
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


        # iterative dfs - stack
        # pre order traversal, bottom up, children processed first
        # o(n) time and o(n) space

        if not root:
            return 0

        stack = [[root, 1]]
        maxDepth = 0

        while stack:
            node, d = stack.pop()

            maxDepth = max(maxDepth, d)

            if node.left:
                stack.append([node.left, d+1])

            if node.right:
                stack.append([node.right, d+1])

        return maxDepth
