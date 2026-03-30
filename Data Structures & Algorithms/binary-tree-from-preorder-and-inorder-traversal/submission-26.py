# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # if not preorder or not inorder:
        #     return None
        
        # root_val = preorder[0]
        # root = TreeNode(root_val)
        # mid = inorder.index(root_val)

        # root.left = self.buildTree(preorder[1:mid+1], inorder[:mid] )
        # root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:] )
        # return root

        if not preorder or not inorder:
            return None

        dfs_inorder_hp = {v:i for i,v in enumerate(inorder)}
        self.index = 0

        def dfs(left, right):
            if left > right:
                return None

            root_val = preorder[self.index]
            root = TreeNode(root_val)
            mid = dfs_inorder_hp[root_val]
            self.index += 1
            root.left = dfs(left, mid-1)
            root.right = dfs(mid+1, right)
            return root

        return dfs(0, len(inorder)-1)


            


        