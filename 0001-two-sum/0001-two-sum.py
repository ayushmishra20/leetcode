class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prev_map = {} 

        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev_map:
                return [prev_map[diff], i]
            prev_map[num] = i
        
        return []