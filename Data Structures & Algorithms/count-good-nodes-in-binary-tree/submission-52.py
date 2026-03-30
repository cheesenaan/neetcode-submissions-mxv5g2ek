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

            good = 1 if node.val >= max_so_far else 0
            new_max = max(node.val, max_so_far)
            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)
            return good

        def dfs_iterative(node, max_so_far):
            stack = []
            stack.append([node, max_so_far])
            good = 0
            while stack:
                cur , max_so_far = stack.pop()
                if not cur:
                    continue 
                if cur.val >= max_so_far:
                    good += 1
                new_max = max(cur.val, max_so_far)
                stack.append([cur.left, new_max])
                stack.append([cur.right, new_max])
            return good

        return dfs_iterative(root, root.val)


        
        