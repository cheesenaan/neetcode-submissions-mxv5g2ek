# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:


        # recursive DFS
        # # if not root:
        # #     return None

        # # root.left, root.right = root.right, root.left

        # # self.invertTree(root.left)
        # # self.invertTree(root.right)

        # iterative DFS (stack: first in last out)

        # # if not root:
        # #     return None

        # # stack = [root]

        # # while stack:
        # #     node = stack.pop()

        # #     node.left, node.right = node.right, node.left

        # #     if node.left:
        # #         stack.append(node.left)

        # #     if node.right:
        # #         stack.append(node.right)

        # BFS (queue : first in first out)
        if not root:
            return root

        from collections import deque

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return root



