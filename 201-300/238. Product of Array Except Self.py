class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        詳細版本，顯示每一步的計算過程
        """
        n = len(nums)
        answer = [1] * n
        
        # 第一遍：左邊乘積
        for i in range(1, n):
            answer[i] = answer[i-1] * nums[i-1]
        
        # 第二遍：右邊乘積
        right_product = 1
        for i in range(n-1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]

        return answer