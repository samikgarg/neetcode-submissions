class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prevProducts = new int[nums.length];
        int[] nextProducts = new int[nums.length];
        int[] result = new int[nums.length];

        prevProducts[0] = nums[0];
        nextProducts[nextProducts.length - 1] = nums[nums.length - 1];
        for (int i = 1; i < nums.length; i++){
            prevProducts[i] = prevProducts[i - 1] * nums[i];
            nextProducts[nums.length - i - 1] = nums[nums.length - i - 1] * nextProducts[nums.length - i];
        }

        result[0] = nextProducts[1];
        result[nums.length - 1] = prevProducts[nums.length - 2];
        for (int i = 1; i < nums.length - 1; i++) {
            result[i] = prevProducts[i - 1] * nextProducts[i + 1];
        }
        return result;
    }
}  
