class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int max = 0;

        while (left < right) {
            int currArea = (right-left)*(Math.min(heights[left], heights[right]));
            if (currArea > max) {
                max = currArea;
            }
            if (heights[right] < heights[left]) {
                right--;
            } else {
                left++;
            }
        }
        return max;
    }
}
