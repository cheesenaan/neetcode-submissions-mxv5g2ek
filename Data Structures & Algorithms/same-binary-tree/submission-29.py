# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        

        def dfs(p, q):
            
            stack = []
            stack.append([p, q])
            while stack:
                pp, qq = stack.pop()
                if not pp and not qq:
                    continue
                if (not pp and qq) or (pp and not qq) or (pp.val != qq.val):
                    return False
                stack.append([pp.left, qq.left])
                stack.append([pp.right, qq.right])
            return True
        return dfs(p,q)
                


        
        