# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # dfs(root)
        # return res       

        if not root:
            return 0

        stack = []
        stack.append([root, False])
        hp = {} # node : height
        res = 0
        while stack:
            cur, v = stack.pop()
            if v:
                left_h = hp.get(cur.left, 0)
                right_h = hp.get(cur.right, 0)
                res = max(res, left_h + right_h)
                hp[cur] = 1 + max(left_h , right_h)
            else:
                stack.append([cur, True])
                if cur.left:
                    stack.append([cur.left, False])
                if cur.right:
                    stack.append([cur.right, False])
        return res




        
        