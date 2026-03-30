# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        stack_p = [p]
        stack_q = [q]

        while stack_p and stack_q:
            node_p = stack_p.pop()
            node_q = stack_q.pop()

            if node_p and not node_q:
                return False

            if node_q and not node_p:
                return False

            if not node_p and not node_q:
                continue 

            if node_p.val != node_q.val:
                return False

            stack_p.append(node_p.right)

            stack_p.append(node_p.left)

            stack_q.append(node_q.right)

            stack_q.append(node_q.left)


        if stack_p or stack_q:
            return False

        return True