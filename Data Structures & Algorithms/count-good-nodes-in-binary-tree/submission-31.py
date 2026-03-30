# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        # good = 0
        # def dfs(node, max_so_far):
        #     nonlocal good

        #     if not node:
        #         return 0

        #     good += 1 if node.val >= max_so_far else 0
        #     new_max = max(node.val, max_so_far)

        #     dfs(node.left, new_max)
        #     dfs(node.right, new_max)

        # dfs(root, root.val)
        # return good

        if not root:
            return 0

        stack = [[root, root.val]]
        good = 0

        while stack:
            node, max_so_far = stack.pop()

            good += 1 if node.val >= max_so_far else 0

            new_max = max(node.val, max_so_far)

            if node.left:
                stack.append([node.left, new_max])

            if node.right:
                stack.append([node.right, new_max])

        return good

