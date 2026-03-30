# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # # O(n) time and space
        # # recursive
        # if not root:
        #     return

        # root.left, root.right = root.right, root.left
        # self.invertTree(root.left)
        # self.invertTree(root.right)
        # return root

        # O(n) time and space
        # dfs 
        # if not root:
        #     return

        # stack = []
        # stack.append(root)
        # while stack:
        #     node = stack.pop()
        #     node.left, node.right = node.right, node.left
        #     if node.left:
        #         stack.append(node.left)
        #     if node.right:
        #         stack.append(node.right)
        # return root

        # O(n) time and space
        # bfs 
        if not root:
            return

        q = deque()
        q.append(root)
        while q:
            node = q.popleft()
            node.left, node.right = node.right, node.left
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return root



        