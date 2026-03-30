# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # def dfs(root, maxVal):

        #     if not root:
        #         return 0

        #     res = 1 if root.val >= maxVal else 0
        #     maxVal = max(maxVal, root.val)
        #     res += dfs(root.left, maxVal)
        #     res += dfs(root.right, maxVal)

        #     return res

        # return dfs(root, root.val)

        if not root:
            return 0

        q = deque([[root, root.val]])
        res = 0

        while q:
            node, maxV = q.popleft()

            if node.val >= maxV:
                res += 1
                maxV = node.val


            if node.left:
                q.append([node.left, maxV])

            if node.right:
                q.append([node.right, maxV])

        return res