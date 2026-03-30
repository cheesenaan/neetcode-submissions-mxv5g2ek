# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Time complexity: O ( n ) O(n) Space complexity: O ( h ) O(h) Best Case (balanced tree): O ( l o g ( n ) ) O(log(n)) Worst Case (degenerate tree): O ( n ) O(n)

        # maxD = 0

        # def dfs(node):
        #     nonlocal maxD

        #     if not node:
        #         return 0

        #     left_h = dfs(node.left)
        #     right_h = dfs(node.right)
        #     maxD = max(maxD, left_h + right_h)
        #     return 1 + max(left_h, right_h)

        # dfs(root)
        # return maxD

        if not root:
            return 0

        stack = [[root, False]]
        h = {} # node : height
        maxD = 0

        while stack:
            node, v = stack.pop()
            if v == True:
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



        
        
        