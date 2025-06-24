# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        values = []

        def inorder(node):
            if not node:
                return 
            inorder(node.left)
            values.append(node.val)
            inorder(node.right)
        inorder(root)

        dummy = TreeNode(0)
        current = dummy

        for i in values:
            current.right = TreeNode(i)
            current = current.right

        return dummy.right