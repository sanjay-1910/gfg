
class Solution:
    def pal(self, s, i, j, dp):
        if i > j:
            return ""
        if i == j:
            return s[i]
        if dp[i][j] != -1:
            return dp[i][j]
        
        if s[i] == s[j]:
            mid = self.pal(s, i+1, j-1, dp)
            if len(mid) == (j - 1 - i):  # Corrected length condition
                dp[i][j] = s[i] + mid + s[j]
                return dp[i][j]
        
        # Ensure `left` and `right` are always defined
        left = self.pal(s, i, j-1, dp)
        right = self.pal(s, i+1, j, dp)

        if len(left) >= len(right):
            dp[i][j] = left
        else:
            dp[i][j] = right
        return dp[i][j]

    def longestPalindrome(self, s):
        dp = [[-1] * len(s) for _ in range(len(s))]
        return self.pal(s, 0, len(s)-1, dp)


# Driver Code


        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends