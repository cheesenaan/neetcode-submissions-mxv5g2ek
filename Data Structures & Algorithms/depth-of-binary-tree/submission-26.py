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

        q = deque([[root, 0]])
        maxDepth = 0

        while q:
            for i in range(len(q)):
                node, depth = q.popleft()

                maxDepth = max(maxDepth, depth)

                if node.left:
                    q.append([node.left, depth+1])

                if node.right:
                    q.append([node.right, depth+1])
            
            maxDepth = maxDepth + 1


        return maxDepth


        