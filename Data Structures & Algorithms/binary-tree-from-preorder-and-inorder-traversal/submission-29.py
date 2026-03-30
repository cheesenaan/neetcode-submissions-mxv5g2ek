# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        
        ############################## SOLUTION 1 ####################################
        def solution_1():
            # O(n^2) time and O(n) space
            if not preorder or not inorder:
                return None

            # inorder = dfs
            # preoder = bfs

            # preoder[0] is always root
            root_val = preorder[0]
            root = TreeNode(root_val)
            mid = inorder.index(root_val)
            root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
            root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
            return root

        ############################## SOLUTION 2 ####################################
        
        if not preorder or not inorder:
            return None
        
        dfs_inorder_hp = {n:i for i,n in enumerate(inorder)}
        print("dfs_inorder_hp is ", dfs_inorder_hp)
        self.i = 0

        def dfs(l, r):
            if l > r:
                return 

            root_val = preorder[self.i]
            root = TreeNode(root_val)
            mid = dfs_inorder_hp[root_val]
            self.i += 1
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root

        return dfs(0, len(inorder)-1)

        

        