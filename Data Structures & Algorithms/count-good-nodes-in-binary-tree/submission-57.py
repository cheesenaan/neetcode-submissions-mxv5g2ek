# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(node, max_so_far):
            if not node:
                return 0

            res = 1 if node.val >= max_so_far else 0
            new_max = max(node.val, max_so_far)
            res += dfs(node.left, new_max)
            res += dfs(node.right, new_max)
            return res

        # return dfs(root,-float('inf'))    

        stack = [[root,root.val]]
        res = 0
        while stack:
            node, max_so_far = stack.pop()

            if not node:
                continue 

            if node.val >= max_so_far:
                res += 1

            new_max = max(node.val, max_so_far)
            stack.append([node.left, new_max])
            stack.append([node.right, new_max])

        return res


