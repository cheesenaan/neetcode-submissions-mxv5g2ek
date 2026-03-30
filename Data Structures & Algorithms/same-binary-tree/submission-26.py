# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q:
        #     return True
        # if (p and not q) or (not p and q):
        #     return False
        # if p and q and p.val != q.val:
        #     return False
        # return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        if (p and not q) or (not p and q):
            return False
        if p and q and p.val != q.val:
            return False

        stack = [[p,q]]

        while stack:
            pp, qq = stack.pop()

            if not pp and not qq:
                continue 
            if (pp and not qq) or (not pp and qq) or (pp and qq and pp.val != qq.val):
                return False

            stack.append([pp.left, qq.left])
            stack.append([pp.right, qq.right])

        return True


