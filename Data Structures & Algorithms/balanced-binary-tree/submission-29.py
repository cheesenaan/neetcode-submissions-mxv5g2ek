# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root:
            return True

        stack = []
        stack.append([root, False])
        hp = {} # node : height
        while stack:
            cur, v = stack.pop()
            if v:
                left_h = hp.get(cur.left, 0)
                right_h = hp.get(cur.right, 0)
                if abs(left_h-right_h) > 1:
                    return False
                hp[cur] = 1 + max(left_h , right_h)
            else:
                stack.append([cur, True])
                if cur.left:
                    stack.append([cur.left, False])
                if cur.right:
                    stack.append([cur.right, False])

        return True


        