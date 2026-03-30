# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        # pre order traversal 

        # recursive dfs

        # def dfs(node, maxVal):

        #     if not node:
        #         return 0

        #     res = 1 if node.val >= maxVal else 0

        #     maxVal = max(node.val, maxVal)

        #     res += dfs(node.left, maxVal)
        #     res += dfs(node.right, maxVal)

        #     return res

        # return dfs(root, root.val)

        # dfs iterative - stack - FILO

        stack = [[root, root.val]]
        res = 0
        maxVal = 0

        while stack:
            node, maxVal = stack.pop()

            if node.val >= maxVal:
                res += 1

            maxVal = max(maxVal, node.val)

            if node.left:
                stack.append([node.left, maxVal])

            if node.right:
                stack.append([node.right, maxVal]) 

        return res           