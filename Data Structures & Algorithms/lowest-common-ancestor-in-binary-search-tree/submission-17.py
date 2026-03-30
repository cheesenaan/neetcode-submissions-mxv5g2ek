# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # if not p or not q or not root:
        #     return root

        # if min(p.val, q.val) > root.val:
        #     return self.lowestCommonAncestor(root.right, p, q)
        # elif max(p.val, q.val) < root.val:
        #     return self.lowestCommonAncestor(root.left, p, q)
        # else:
        #     return root

        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr=curr.left
            else:
                return curr
        