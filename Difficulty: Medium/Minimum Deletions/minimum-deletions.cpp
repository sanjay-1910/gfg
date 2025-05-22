class Solution {
  public:
int lps(string& s, int i, int j, vector<vector<int>>& dp) {
        if (i > j) return 0;
        if (i == j) return 1;
        if (dp[i][j] != -1) return dp[i][j];

        if (s[i] == s[j]) {
            dp[i][j] = 2 + lps(s, i + 1, j - 1, dp);
        } else {
            dp[i][j] = max(lps(s, i + 1, j, dp), lps(s, i, j - 1, dp));
        }
        return dp[i][j];
    }
    int minDeletions(string s) {
       int n = s.size();
        vector<vector<int>> dp(n, vector<int>(n, -1));
        int lenLPS = lps(s, 0, n - 1, dp);
        return n - lenLPS;
    }
};