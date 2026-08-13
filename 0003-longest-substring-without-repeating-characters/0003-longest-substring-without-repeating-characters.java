class Solution {
    public int lengthOfLongestSubstring(String s) {
        int[] lastIndex = new int[128];
        // Initialize all indices to -1 (unseen)
        java.util.Arrays.fill(lastIndex, -1);

        int left = 0, maxLength = 0;

        for (int right = 0; right < s.length(); right++) {
            char currentChar = s.charAt(right);

            // If character was seen inside current window, jump left pointer
            if (lastIndex[currentChar] >= left) {
                left = lastIndex[currentChar] + 1;
            }

            // Record current character's latest index
            lastIndex[currentChar] = right;
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}