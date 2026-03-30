# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def dfs(node, max_so_far):
            if not node:
                return 0

            good = 1 if node.val >= max_so_far else 0
            new_max = max(node.val, max_so_far)

            good += dfs(node.left, new_max)
            good += dfs(node.right, new_max)

            return good

        return dfs(root, root.val)

        # if not root:
        #     return 0

        # q = deque([[root, root.val]])
        # cnt = 0

        # while q:
        #     node, max_so_far = q.popleft()

        #     if node.val >= max_so_far:
        #         cnt += 1

        #     new_max = max(node.val, max_so_far)

        #     if node.left:
        #         q.append([node.left, new_max])

        #     if node.right:
        #         q.append([node.right, new_max])

        # return cnt



                
            