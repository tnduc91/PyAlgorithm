'REF: https://leetcode.com/problems/minimum-distance-between-bst-nodes'

import TreeNode

class MinimumDistanceBST:
    def minDiffInBST(self, root:TreeNode) -> int:
        vals = []
        def dfs(node):
            if node:
                vals.append(node.val)
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        vals.sort()

        return min(vals[i+1] - vals[i]
                   for i in range(len(vals) - 1))