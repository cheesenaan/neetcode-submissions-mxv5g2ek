# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # recursive dfs
        # o(n) time, o(h) space 
        # if not root:
        #     return root

        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root


        # iterative dfs - stack
        # o(n) time, o(n) space 

        # if not root:
        #     return root

        # stack = [root]

        # while stack:
        #     node = stack.pop()

        #     node.left, node.right = node.right, node.left

        #     if node.right:
        #         stack.append(node.right)

        #     if node.left:
        #         stack.append(node.left)

        # return root

        # dfs - q
        if not root:
            return root

        q = deque([root])

        while q:
            node = q.popleft()

            node.left, node.right = node.right, node.left
            
            if node.right:
                q.append(node.right)

            if node.left:
                q.append(node.left)

        return root




            

        