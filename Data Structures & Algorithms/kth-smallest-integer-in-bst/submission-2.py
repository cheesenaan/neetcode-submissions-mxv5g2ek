# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        
        #in-order traversal (which visits BST nodes in sorted order).
        # o(n) time and o(h) space

 
        # def inOrderDfs(node):
        #     nonlocal k, res

        #     if not node:
        #         return 0

        #     inOrderDfs(node.left)

        #     k = k - 1
        #     if k == 0:
        #         res  = node.val
        #         return 

        #     inOrderDfs(node.right)

        # res = None
        # inOrderDfs(root)
        # return res

        if not root:
            return root

        stack = []
        node = root

        while stack or node:

            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            k = k - 1

            if k == 0:
                return node.val

            node = node.right

        return









            