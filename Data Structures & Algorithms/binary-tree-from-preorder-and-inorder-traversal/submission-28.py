# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        # inorder = dfs
        # preoder = bfs

        # preoder[0] is always root
        root_val = preorder[0]
        root = TreeNode(root_val)
        k = inorder.index(root_val)
        root.left = self.buildTree(preorder[1:k+1], inorder[:k])
        root.right = self.buildTree(preorder[k+1:], inorder[k+1:])
        return root
        

        