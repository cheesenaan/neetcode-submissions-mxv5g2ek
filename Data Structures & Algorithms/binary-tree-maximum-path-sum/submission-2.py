# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:


        # res = float('-inf')

        # def dfs(node):
        #     nonlocal res

        #     if not node:
        #         return 0

        #     maxLeft = max(dfs(node.left), 0)
        #     maxRight = max(dfs(node.right), 0)

        #     # update global max
        #     res = max(res, maxLeft + maxRight + node.val)

        #     # return best path upward
        #     return node.val + max(maxLeft , maxRight)

        # dfs(root)
        # return res


        if not root:
            return 0

        stack = [[root, False]]
        hp = {} # node -> best max
        res = float('-inf')

        while stack:
            node, v = stack.pop()

            if v:
                maxLeft = max(hp.get(node.left, 0), 0)
                maxRight = max(hp.get(node.right, 0), 0)
                res = max(res, maxLeft + maxRight + node.val)
                hp[node] = node.val + max(maxLeft , maxRight)
            else:
                stack.append([node, True])
                if node.left:
                    stack.append([node.left, False])
                if node.right:
                    stack.append([node.right, False])

        return res