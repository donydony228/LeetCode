# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        # 用來儲存結果的變數
        self.min_diff = float('inf')  # 初始設為無限大
        self.pre_val = None          # 儲存前一個節點的值
        
        def inorder_traversal(node):
            if not node:
                return None

            inorder_traversal(node.left)

            if self.pre_val is not None:
                current_dif = node.val - self.pre_val
                self.min_diff = min(self.min_diff, current_dif)
            
            self.pre_val = node.val

            inorder_traversal(node.right)

        
        inorder_traversal(root)
        return self.min_diff