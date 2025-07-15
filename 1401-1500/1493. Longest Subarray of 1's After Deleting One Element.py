class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        zero_count = 0
        max_length = 0
        
        # 右指針遍歷整個陣列
        for right in range(len(nums)):
            # 如果當前元素是0，增加zero_count
            if nums[right] == 0:
                zero_count += 1
            
            # 當窗口內0的個數超過k時，收縮左邊界
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # 更新最大長度
            max_length = max(max_length, right - left + 1)
        
        return max_length - 1