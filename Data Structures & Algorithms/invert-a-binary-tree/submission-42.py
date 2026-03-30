# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        # recursive 
        # time : O(n)
        # space : O(h), O(n) worst case skweed tree, O(logn) best case balanced tree
        # if not root:
        #     return root

        # root.left, root.right = root.right, root.left

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root

        # DFS
        # O(n) time
        # O(n) space worst case skweed, O(logn) best case balanced 

        # if not root:
        #     return root

        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     node.left, node.right = node.right, node.left

        #     if node.left:
        #         stack.append(node.left)

        #     if node.right:
        #         stack.append(node.right)

        # return root

        # BFS
        # O(n) time
        # O(n) space worst case skweed, O(logn) best case balanced 


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



        