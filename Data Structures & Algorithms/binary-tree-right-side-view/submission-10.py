# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []

        q = deque()
        q.append(root)
        res = []
        while q:
            level = []
            tmp = None
            for i in range(len(q)):
                cur = q.popleft()
                tmp = cur.val
                level.append(cur.val)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            res.append(tmp)

        return res

        