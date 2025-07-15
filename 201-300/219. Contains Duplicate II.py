class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        maps = {}

        for i in range(len(nums)):
            if nums[i] in maps and abs(i - maps[nums[i]]) <= k:
                return True
            maps[nums[i]] = i
        
        return False