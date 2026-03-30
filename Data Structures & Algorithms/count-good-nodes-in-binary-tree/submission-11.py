# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        # def dfs(node, maxV):
        #     if not node:
        #         return 0

        #     res = 1 if node.val >= maxV else 0

        #     maxV = max(node.val, maxV)

        #     res += dfs(node.left, maxV)
        #     res += dfs(node.right, maxV)

        #     return res


        # return dfs(root, root.val)

        if not root:
            return 0


        stack = [[root, root.val]]
        res = 0

        while stack:
            node, m = stack.pop()

            if node.val >= m:
                res = res + 1

            m = max(m, node.val)

            if node.left:
                stack.append([node.left, m])
            
            if node.right:
                stack.append([node.right, m])

        return res
            




            


        