# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # recusrive dfs

        # if not root:
        #     return 0

        # return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # dfs interative - stack

        if not root:
            return 0

        stack = [[root, 1]]
        level = 0

        while stack:
            node, l = stack.pop()
            level = max(level, l)

            if node.left:
                stack.append([node.left, l+1])

            if node.right:
                stack.append([node.right, l+1])

            
        return level

        # bfs q

        # if not root:
        #     return 0

        # q = deque([[root, 0]])
        # level = 0

        # while q:
        #     for i in range(len(q)):
        #         node , l = q.popleft()
        #         level = max(level, l)

        #         if node.left:
        #             q.append([node.left, level + 1])
        #         if node.right:
        #             q.append([node.right, level + 1])

        #     level = level + 1

        
        return level



        