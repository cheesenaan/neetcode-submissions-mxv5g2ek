# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        good = 0
        max_so_far = 0

        def dfs(node, max_so_far):
            nonlocal good

            if not node:
                return 

            good += 1 if node.val >= max_so_far else 0

            new_max = max(node.val, max_so_far)

            dfs(node.left, new_max)        
            dfs(node.right, new_max)      

        dfs(root, root.val)
        return good
        