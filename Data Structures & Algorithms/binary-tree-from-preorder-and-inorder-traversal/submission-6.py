# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # preorder = bfs = [root, left, right]
        # inorder = dfs = [left, root, right]

        # if not preorder or not inorder:
        #     return None

        # root = TreeNode(preorder[0])
        # mid = inorder.index(preorder[0])

        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        # return root

        dfs_inorder_index = {v:i for i,v in enumerate(inorder)}
        self.pre_idx = 0


        if not preorder or not inorder:
            return None

        def dfs(left, right):
            if left > right:
                return 

            root_value = preorder[self.pre_idx]
            root = TreeNode(preorder[self.pre_idx])
            mid = dfs_inorder_index[root_value]
            self.pre_idx += 1

            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)
            return root

        return dfs(0, len(inorder)-1)

            