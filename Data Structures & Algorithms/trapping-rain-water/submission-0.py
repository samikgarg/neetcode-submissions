class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = []
        right_max = []
        left_max.append(height[0])
        right_max.append(height[-1])
        for i in range(1, len(height)):
            left_max.append(max(left_max[i - 1], height[i]))
            right_max.insert(0, max(height[-i - 1], right_max[-i]))
        
        total = 0
        for i, h in enumerate(height):
            total += min(left_max[i], right_max[i]) - h
        return total