# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        

        # bfs - O(n) time and space
        if not root:
            return 0

        q = deque()
        q.append([root, 1])
        res = 0
        while q:
            cur, d = q.popleft()
            res = max(res, d)

            if cur.left:
                q.append([cur.left, d+1])

            if cur.right:
                q.append([cur.right, d+1])

        return res


            



        
        