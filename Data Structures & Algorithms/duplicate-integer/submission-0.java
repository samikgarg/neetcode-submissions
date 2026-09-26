class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashSet<Integer> found = new HashSet<>();

        for (int i = 0; i < nums.length; i++) {
            if (found.contains(nums[i])) {
                return true;
            }
            found.add(nums[i]);
        }

        return false;
    }
}
