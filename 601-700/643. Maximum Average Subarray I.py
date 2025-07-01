class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp_sum = max_sum = sum(nums[:k])

        for i in range(k, len(nums)):
            temp_sum += nums[i] - nums[i-k]
            max_sum = max(temp_sum, max_sum)
        return max_sum / k