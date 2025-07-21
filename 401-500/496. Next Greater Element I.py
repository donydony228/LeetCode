class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 第一步：使用Stack為nums2中每個元素找下一個更大元素
        stack = []  # 單調遞減堆疊
        next_greater = {}  # 儲存每個元素的下一個更大元素
        
        # print("=== 使用Stack處理nums2 ===")
        
        for num in nums2:
            # print(f"\n處理元素: {num}")
            # print(f"當前stack: {stack}")
            
            # 當stack不為空且當前元素大於stack頂端時
            while stack and num > stack[-1]:
                smaller = stack.pop()  # pop出較小的元素
                next_greater[smaller] = num  # 記錄它的下一個更大元素
                # print(f"  找到 {smaller} 的下一個更大元素: {num}")
            
            stack.append(num)  # 將當前元素push進stack
            # print(f"  push {num} 進stack，現在stack: {stack}")
        
        # stack中剩餘的元素都沒有下一個更大元素
        while stack:
            remaining = stack.pop()
            next_greater[remaining] = -1
            # print(f"  {remaining} 沒有下一個更大元素")
        
        # print(f"\n完整的next_greater映射: {next_greater}")
        
        # 第二步：根據nums1查詢結果
        result = [next_greater[num] for num in nums1]
        # print(f"最終結果: {result}")
        
        return result