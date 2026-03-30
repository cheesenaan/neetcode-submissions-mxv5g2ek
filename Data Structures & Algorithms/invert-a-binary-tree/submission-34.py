# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # dfs recursive - O(n) time, O(h) space - nlogn best case on worst case
        
        # if not root:
        #     return root

        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        if not root:
            return root

        q = deque([root])

        while q:
            node = q.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)

        return root



        



        