# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # post order traversal, dfs, stack, FILO, bottom up using height being returned
        if not root:
            return 0

        stack = [[root, False]]
        h = {} # node address : height of node
        maxD = 0 

        while stack:
            node, visited = stack.pop()

            if visited:
                left_h = h.get(node.left, 0)
                right_h = h.get(node.right, 0)
                maxD = max(maxD, left_h + right_h)
                h[node] = 1 + max(left_h, right_h)
            else:
                stack.append([node, True])
                if node.left:
                    stack.append([node.left, False])
                if node.right:
                    stack.append([node.right, False])

        return maxD



        
        