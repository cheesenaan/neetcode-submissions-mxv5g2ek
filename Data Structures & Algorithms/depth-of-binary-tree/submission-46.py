# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # recursive. O(n) time and O(h) space. best case space logn for balanced tree, worst case n degenerate tree
        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # iterative dfs, stack

        
        # if not root:
        #     return 0

        # stack = [[1, root]]
        # maxDepth = 0

        # while stack:
        #     depth, node = stack.pop()
        #     maxDepth = max(maxDepth, depth)

        #     if node.left:
        #         stack.append([depth+1, node.left])

        #     if node.right:
        #         stack.append([depth+1, node.right])

        # return maxDepth


        # bfs
        if not root:
            return 0

        q = deque([[1, root]])
        maxDepth = 0

        while q:
            depth, node = q.popleft()
            maxDepth = max(maxDepth, depth)

            if node.left:
                q.append([depth+1, node.left])

            if node.right:
                q.append([depth+1, node.right])

        return maxDepth

        