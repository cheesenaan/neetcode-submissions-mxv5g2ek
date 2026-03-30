# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        
        
        
        # Maximum Depth of Binary Tree = height
        res = 0
        def dfs(root):
            nonlocal res

            if not root:
                return 0

            left_h = dfs(root.left)
            right_h = dfs(root.right)
            h = max(left_h, right_h) + 1
            res = max(res, h)
            return h

       
        
        def bfs(root):
            if not root:
                return 0

            q = deque()
            q.append(root)
            res = 0
            while q:
                for i in range(len(q)):
                    cur = q.popleft()
                    if cur.left:
                        q.append(cur.left)
                    if cur.right:
                        q.append(cur.right)
                res += 1
            return res

        return bfs(root)