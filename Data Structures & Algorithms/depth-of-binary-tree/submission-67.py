# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        ############################## solution 1 ################################
        # o(n) time and o(h) space - best case nlogn, worst case n
        res = 0
        def dfs_recursive(node):
            nonlocal res
            if not node:
                return 0

            left_h = dfs_recursive(node.left)
            right_h = dfs_recursive(node.right)
            h = 1 + max(left_h, right_h)
            res = max(h, res)
            return h

        # dfs_recursive(root)    
        # return res

        ############################## solution 2 ################################
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

        



        
        
        