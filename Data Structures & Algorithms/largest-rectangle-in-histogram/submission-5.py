class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        left_areas = [1] * len(heights)
        right_areas = [1] * len(heights)

        stack_left = [(heights[0], 0)]
        stack_right = [(heights[-1], len(heights) - 1)]

        for curr_index in range (1, len(heights)):
            curr_height = heights[curr_index]
            prev_height, prev_index = stack_left.pop()
            while prev_height >= curr_height:
                if len(stack_left) == 0:
                    prev_height, prev_index = 0, -1
                    break
                else:
                    prev_height, prev_index = stack_left.pop()
            left_areas[curr_index] = curr_index - prev_index
            if prev_index != -1:
                stack_left.append((prev_height, prev_index))
            stack_left.append((curr_height, curr_index))

            curr_index_right = len(heights) - curr_index - 1
            curr_height = heights[curr_index_right]
            prev_height, prev_index = stack_right.pop()
            while prev_height >= curr_height:
                if len(stack_right) == 0:
                    prev_height, prev_index = 0, len(heights)
                    break
                else:
                    prev_height, prev_index = stack_right.pop()
            right_areas[curr_index_right] = prev_index - curr_index_right
            if prev_index != len(heights):
                stack_right.append((prev_height, prev_index))
            stack_right.append((curr_height, curr_index_right))
            

        max_area = 0
        for i in range(len(heights)):
            curr_area = (left_areas[i] + right_areas[i] - 1) * heights[i]
            if curr_area > max_area:
                max_area = curr_area
        
        return max_area

