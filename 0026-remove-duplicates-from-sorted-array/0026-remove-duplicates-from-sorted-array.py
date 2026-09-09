class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        write_idx = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                nums[write_idx] = nums[i]
                write_idx += 1
            pass
        return write_idx