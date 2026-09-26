class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> numSet = arrToSet(nums);
        int longest = 0;

        for (int num : nums) {
            if (!numSet.contains(num - 1)) {
                int length = 0;
                int currNum = num;
                while (numSet.contains(currNum)) {
                    length += 1;
                    currNum++;
                }
                if (length > longest) {
                    longest = length;
                }
            }
        }

        return longest;

    }

    private HashSet<Integer> arrToSet (int[] arr) {
        HashSet<Integer> set = new HashSet<>();
        for (int i : arr) {
            set.add(i);
        }
        return set;
    }
}
