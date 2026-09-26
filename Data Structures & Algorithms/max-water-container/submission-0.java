class Solution {
    public int maxArea(int[] heights) {
        int[] dp = new int[heights.length];
        dp[0] = 0;
        dp[1] = Math.min(heights[0], heights[1]);
        int maxSoFar = Math.max(heights[0], heights[1]);

        for (int i = 2; i < dp.length; i++) {
            int currMax = 0;
            for (int j = 0; j < i; j++) {
                if ((i-j)*(Math.min(heights[i], heights[j])) > currMax) {
                    currMax = (i-j)*(Math.min(heights[i], heights[j]));
                }
            }
            dp[i] = Math.max(dp[i-1], currMax);
        }

        return dp[dp.length-1];
    }
}
