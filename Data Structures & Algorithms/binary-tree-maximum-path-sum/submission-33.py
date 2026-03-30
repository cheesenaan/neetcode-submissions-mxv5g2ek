class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        # We ignore negative child paths (max(..., 0)) because any negative sum would only
        # reduce the total path value, and paths are allowed to stop at any node.


        # Global result to store the maximum path sum found anywhere in the tree
        # Start with -inf because values can be negative
        res = -float('inf')

        def dfs(root):
            nonlocal res

            # Base case:
            # If node is None, it contributes 0 to the path
            # (we don't want missing nodes to reduce the sum)
            if not root:
                return 0

            # Recursively compute max gain from left subtree
            # If the subtree gives a negative sum, discard it by taking 0
            left_h = max(dfs(root.left), 0)

            # Recursively compute max gain from right subtree
            # Again, ignore negative paths
            right_h = max(dfs(root.right), 0)

            # Case where the path passes through the current node
            # left subtree -> current node -> right subtree
            # This is a "complete" path, so we update the global answer
            res = max(res, root.val + left_h + right_h)

            # Return the maximum gain that this node can contribute to its parent
            # We can only choose ONE direction (left or right), not both
            return root.val + max(left_h, right_h)

        # Start DFS from root
        dfs(root)

        # Return the maximum path sum found in the entire tree
        return res
