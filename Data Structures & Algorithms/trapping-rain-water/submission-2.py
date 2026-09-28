class Solution:
    def trap(self, height: List[int]) -> int:
        
        left_maximums = [0] * len(height)
        left_maximums[0] = height[0]
        for i in range(1, len(height)):
            left_maximums[i] = max(height[i], left_maximums[i - 1])
        
        right_maximums = [0] * len(height)
        right_maximums[-1] = height[-1]
        for i in range(len(height) - 2, -1, -1):
            right_maximums[i] = max(height[i], right_maximums[i + 1])
        
        res = 0
        for i in range(len(height)):
            res += min(left_maximums[i], right_maximums[i]) - height[i]
        
        return res