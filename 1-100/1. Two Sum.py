class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, value in enumerate(nums):
            k = target - value
            if k in seen:
                return [seen[k], i]
            
            seen[value] = i

        return None
