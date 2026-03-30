# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:

        res = []

        def dfs(node):
            if not node:
                res.append('N')
                return 
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
            return node
        
        dfs(root)
        return ','.join(res)


    def deserialize(self, data: str) -> Optional[TreeNode]:

        vals = data.split(',')
        self.index = 0

        def dfs():
            if vals[self.index] == 'N':
                self.index += 1
                return None
            node = TreeNode(vals[self.index])
            self.index += 1
            node.left, node.right = dfs(), dfs()
            return node

        return dfs()

