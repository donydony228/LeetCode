# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('inf')
        self.pre_val = None

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)

            if self.pre_val is not None:
                self.min_diff = min(self.min_diff, node.val - self.pre_val)

            self.pre_val = node.val

            inorder(node.right)

        inorder(root)
        return self.min_diff 