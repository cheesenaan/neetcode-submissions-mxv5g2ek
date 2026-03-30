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

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))



        # DFS iterative - stack - first in last out

        # if not root:
        #     return 0

        # stack = [[root, 1]]
        # maxDepth = 0

        # while stack:
        #     node , depth = stack.pop()

        #     maxDepth = max(maxDepth, depth)

        #     if node.left:
        #         stack.append([node.left, depth + 1])

        #     if node.right:
        #         stack.append([node.right, depth + 1])
        
        # return maxDepth



        # bfs - queue - level by level - first in first out
        
        
        # if root is None:
        #     return 0

        # q = deque([root])
        # level = 0

        # while q:
        #     for i in range(len(q)):
        #         node = q.popleft()

        #         if node.left:
        #             q.append(node.left)

        #         if node.right:
        #             q.append(node.right)

        #     level = level + 1

        # return level


        