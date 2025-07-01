class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        oper_num = 0
        
        while left< right:
            cur_sum = nums[left] + nums[right]
            if cur_sum == k:
                oper_num += 1
                left += 1
                right -= 1
            elif cur_sum < k:
                left += 1
            else:
                right -= 1

        return oper_num