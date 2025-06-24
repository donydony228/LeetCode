# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        def inorder(node, arr):
            if not node:
                return None
            inorder(node.left, arr)
            arr.append(node.val)
            inorder(node.right, arr)

        values = []
        inorder(root, values)

        left, right = 0, len(values) - 1
        while left < right:
            total = values[left] + values[right]

            if total == k:
                return True
            elif total < k:
                left += 1
            else:
                right -= 1
        
        return False