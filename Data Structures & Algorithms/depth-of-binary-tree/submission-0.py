# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        q = deque([root])
        level = 0

        while q:
            for i in range(len(q)):
                # pop all nodes in level
                node = q.popleft()
                # add children of nodes in level
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level = level + 1

        return level
