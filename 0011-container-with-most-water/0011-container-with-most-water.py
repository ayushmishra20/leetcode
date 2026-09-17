class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            # 1. Calculate water held by current boundaries
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_height * current_width
            
            # 2. Update the running maximum
            if current_area > max_water:
                max_water = current_area

            # 3. Move the pointer at the shorter boundary
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water