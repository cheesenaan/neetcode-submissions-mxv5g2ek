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
        # return self.isSameTree(p.left, q.left) and  self.isSameTree(p.right, q.right)

        
        stack = []
        stack.append([p,q])
        while stack:
            p,q = stack.pop()
            if not p and not q:
                continue
            if (p and not q) or (not p and q):
                return False
            if p and q and p.val != q.val:
                return False
            stack.append([p.left, q.left])
            stack.append([p.right, q.right])

        return True



       