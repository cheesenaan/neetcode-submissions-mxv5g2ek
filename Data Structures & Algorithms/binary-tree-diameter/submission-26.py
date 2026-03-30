# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        
        
        res = 0

        def dfs(root):
            nonlocal res

            if not root:
                return 0

            left_h = dfs(root.left)
            right_h = dfs(root.right)
            d = left_h + right_h
            res = max(res, d)
            return 1 + max(left_h, right_h)

        dfs(root)
        return res

        # if not root:
        #     return 0

        # stack = [[root, False]]
        # h = {} # node : height
        # maxD = 0

        # while stack:
        #     node, visited = stack.pop()
        #     if visited == True:
        #         left_h = h.get(node.left, 0)
        #         right_h = h.get(node.right, 0)
        #         maxD = max(maxD, (left_h + right_h))
        #         h[node] = 1 + max(left_h , right_h)
        #     else:
        #         stack.append([node, True])
        #         if node.left:
        #             stack.append([node.left, False])
        #         if node.right:
        #             stack.append([node.right, False])

        # return maxD