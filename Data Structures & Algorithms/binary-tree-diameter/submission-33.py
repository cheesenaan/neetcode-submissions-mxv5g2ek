# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # recursion

        # maxD = 0

        # def dfs(node):
        #     nonlocal maxD

        #     if not root:
        #         return 0

        #     left_h = dfs(node.left) if node.left else 0
        #     right_h = dfs(node.right) if node.right else 0

        #     maxD = max(maxD, left_h + right_h)
        #     return 1 + max(left_h, right_h)

        
        # dfs(root)
        # return maxD

        # bfs
        if not root:
            return 0

        hp = {} # node : height
        maxD = 0
        stack = [[root, False]]

        while stack:
            node, v = stack.pop()

            if v == True:
                left_h = hp.get(node.left, 0)
                right_h = hp.get(node.right, 0)
                maxD = max(maxD, left_h + right_h)
                hp[node] = 1 + max(left_h , right_h)
            else:
                stack.append([node, True])
                if node.left:
                    stack.append([node.left, False])
                if node.right:
                    stack.append([node.right, False])

        return maxD

