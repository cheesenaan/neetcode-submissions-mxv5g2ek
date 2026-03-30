# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        # def dfs(leftV, node, rightV):
        #     if not node:
        #         return True

        #     if not (leftV < node.val < rightV):
        #         return False
            
        #     return dfs(leftV, node.left, node.val) and dfs(node.val, node.right, rightV)

        # return dfs(float('-inf'), root, float('inf'))

        if not root:
            return True
        
        stack = [[float('-inf'), root, float('inf')]]
        while stack:
            leftV, node, rightV = stack.pop()

            if not node:
                return True

            if not (leftV < node.val < rightV):
                return False

            if node.left:
                stack.append([leftV, node.left, node.val])

            if node.right:
                stack.append([node.val, node.right, rightV])

        return True


        