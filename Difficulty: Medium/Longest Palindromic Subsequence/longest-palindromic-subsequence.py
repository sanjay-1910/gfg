#User function Template for python3

class Solution:
    def seq(self,i,j,s,dp):
        if(i==j):
            return 1
        if(i>j):
            return 0
        if(dp[i][j]!=-1):
            return dp[i][j]
        if(s[i] == s[j]):
            dp[i][j] = 2+self.seq(i+1,j-1,s,dp)
        else:
            left = self.seq(i+1,j,s,dp)
            right = self.seq(i,j-1,s,dp)
            ans = max(left,right)
            dp[i][j] = ans
        return dp[i][j]
    def longestPalinSubseq(self, s):
        dp =[[-1]*len(s) for i in range(len(s))]
        return self.seq(0,len(s)-1,s,dp)
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        ob = Solution()
        ans = ob.longestPalinSubseq(s)
        print(ans)
        print("~")
# } Driver Code Ends