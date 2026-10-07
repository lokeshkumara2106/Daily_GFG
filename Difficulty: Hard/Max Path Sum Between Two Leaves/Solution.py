class Solution:
    def maxPathSum(self, root):
        ans = float('-inf')

        def dfs(node):
            nonlocal ans

            if node is None:
                return float('-inf')

            # Leaf node
            if node.left is None and node.right is None:
                return node.data

            left = dfs(node.left)
            right = dfs(node.right)

            # Both children exist:
            # path can connect a leaf from left
            # subtree to a leaf from right subtree
            if node.left and node.right:
                ans = max(ans, left + node.data + right)

                # Return the better leaf path upward
                return node.data + max(left, right)

            # Only left child exists
            if node.left:
                return node.data + left

            # Only right child exists
            return node.data + right

        dfs(root)

        return ans if ans != float('-inf') else -1
