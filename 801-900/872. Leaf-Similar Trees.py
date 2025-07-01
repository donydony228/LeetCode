# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.leaf1 = []
        self.leaf2 = []

        def leaf(node, arr):
            if not node:
                return
            leaf(node.left, arr)
            if not node.left and not node.right:
                arr.append(node.val)
            leaf(node.right, arr)
        
        leaf(root1, self.leaf1)
        leaf(root2, self.leaf2)
        return self.leaf1 == self.leaf2