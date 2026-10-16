# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxVal = float('-inf')

        def maxPathSumHelper(root):
            nonlocal maxVal
            if not root:
                return 0
            val = root.val
            leftval = max(maxPathSumHelper(root.left), 0)
            rightval = max(maxPathSumHelper(root.right), 0)
            maxVal = max(maxVal, val + leftval + rightval)
            return max(leftval, rightval) + val
        
        val = maxPathSumHelper(root)
        return max(maxVal, val)