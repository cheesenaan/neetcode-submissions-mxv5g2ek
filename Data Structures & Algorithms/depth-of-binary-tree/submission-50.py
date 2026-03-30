# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # depth = height = 1 + max(l,r)
        
        
        # recursive 
        # O(n) time 
        # O(n) time worst case, O(logn) time best case
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # dfs 
        # O(n) time 
        # O(n) time worst case, O(logn) time best case

        # if not root:
        #     return 0

        # maxDepth = float('-inf')
        # stack = [[1, root]]

        # while stack:
        #     depth, node = stack.pop()

        #     maxDepth = max(maxDepth, depth)
        #     if node.left:
        #         stack.append([depth+1, node.left])

        #     if node.right:
        #         stack.append([depth+1, node.right])

        # return maxDepth


        # BFS

        if not root:
            return 0

        maxDepth = float('-inf')
        q = deque([[1, root]])

        while q:
            depth, node = q.popleft()

            maxDepth = max(maxDepth, depth)
            if node.left:
                q.append([depth+1, node.left])

            if node.right:
                q.append([depth+1, node.right])

        return maxDepth

        