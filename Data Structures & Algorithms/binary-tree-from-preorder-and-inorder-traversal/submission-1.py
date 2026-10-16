# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        preorderindex = 0
        inorderMap = {}

        for i in range(len(inorder)):
            inorderMap[inorder[i]] = i
        
        def buildTreeHelper(start, end):
            if start > end:
                return None
            nonlocal preorderindex
            val = preorder[preorderindex]
            preorderindex += 1
            root = TreeNode(val)
            inorderindex = inorderMap[val]

            root.left = buildTreeHelper(start, inorderindex - 1)
            root.right = buildTreeHelper(inorderindex + 1, end)
            return root

        root = buildTreeHelper(0, len(preorder) - 1)
        return root
