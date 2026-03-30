# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # recursion, returning height in stack each recurisve call - dfs

        # maxD = 0

        # def dfs(node):
        #     nonlocal maxD

        #     if not node:
        #         return 0

        #     left_h = dfs(node.left)
        #     right_h = dfs(node.right)
        #     maxD = max(maxD, left_h + right_h)
        #     h = 1 + max(left_h, right_h)
        #     return h


        # dfs(root)
        # return maxD


        # iterative dfs
        q = deque([[root, False]])
        hp = {} # node address, height
        maxD = 0

        while q:
            node, visited = q.pop()

            if visited:
                left_h = hp.get(node.left, 0)
                right_h = hp.get(node.right, 0)
                maxD = max(maxD, left_h + right_h)
                hp[node] = 1 + max(left_h, right_h)
            else:
                q.append([node, True])
                if node.left:
                    q.append([node.left, False])
                if node.right:
                    q.append([node.right, False])

        return maxD