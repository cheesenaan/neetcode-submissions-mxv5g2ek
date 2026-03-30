# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # iterative dfs - stack

        # stack with visited boolean flag
        # maxDiamater to store max diameter
        # proccess bottom up with children first

        stack = [[root, False]]
        d = 0
        h = {} # node address : height 

        while stack:
            node , visited = stack.pop()

            if not node:
                continue

            if visited:
                # Post-order step: both children processed
                left = h.get(node.left, 0)
                right = h.get(node.right, 0)
                h[node] = 1 + max(left, right)
                d = max(d, left+right)

            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return d