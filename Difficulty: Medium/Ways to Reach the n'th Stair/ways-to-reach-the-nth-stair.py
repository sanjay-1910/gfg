
class Solution:
    def stairs(self,n,dp):
        if(n == 0):
            # dp[n] = 1
            return 1
        if(n<0):
            # dp[n] = 0
            return 0
        if(dp[n]!=-1):
            return dp[n]
        left = self.stairs(n-1,dp)
        right = self.stairs(n-2,dp)
        dp[n] = left+right
        return dp[n]
    def countWays(self, n):
        dp = [-1]*(n+1)
        ans = self.stairs(n,dp)
        return ans
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

sys.setrecursionlimit(10**6)

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        m = int(input())
        ob = Solution()
        print(ob.countWays(m))

        print("~")

# } Driver Code Ends