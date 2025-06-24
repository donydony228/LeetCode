# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None  # 在 Python 中使用 None 而非 null
        
        def construct(left, right):
            if left >= right:
                return None  # 基本情況：沒有元素時返回 None
                
            mid = (left + right) // 2  # 找出中間位置
            node = TreeNode(nums[mid])  # 創建新節點
            node.left = construct(left, mid)  # 構建左子樹
            node.right = construct(mid + 1, right)  # 構建右子樹
            return node  # 返回構建好的子樹根節點
        
        return construct(0, len(nums))  # 從整個陣列範圍開始構建