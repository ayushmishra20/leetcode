class Solution {
    public int maximumWealth(int[][] accounts) {
        int maxwelth = 0;
        for(int i =0; i < accounts.length; i++){
            int currentCostWelth = 0;
            for( int j = 0; j < accounts[i].length; j++){
                currentCostWelth += accounts[i][j];
            }
            maxwelth = Math.max(maxwelth, currentCostWelth);
        }
        return maxwelth;
    }
}