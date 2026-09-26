class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0;
        int right = numbers.length - 1;

        while (left < right) {
            if (numbers[left] + numbers[right] == target) {
                int[] indices = new int[2];
                indices[0] = left + 1;
                indices[1] = right + 1;
                return indices;
            } else if (numbers[left] + numbers[right] > target) {
                right--;
            } else {
                left++;
            }
        }
        int[] indices = new int[2];
        indices[0] = -1;
        indices[1] = -1;
        return indices;
    }
}
