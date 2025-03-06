class Solution:
    def subseq(self,text1,text2,index1,index2,dp):
        if(index1 == len(text1) or index2 == len(text2)):
            return 0
        if(dp[index1][index2] != -1):
            return dp[index1][index2]
        if(text1[index1] == text2[index2]):
            dp[index1][index2] = 1+self.subseq(text1,text2,index1+1,index2+1,dp)
        else:
            left = self.subseq(text1,text2,index1+1,index2,dp)
            right = self.subseq(text1,text2,index1,index2+1,dp)
            ans = max(left,right)
            dp[index1][index2] = ans
        return dp[index1][index2]
    def lcs(self, s1, s2):
        dp= [[-1]*len(s2) for i in range(len(s1))]
        ans = self.subseq(s1,s2,0,0,dp)
        return ans
        # code here
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        s1 = str(input())  # Take first string as input
        s2 = str(input())  # Take second string as input
        ob = Solution()
        # Call the lcs function and print the result
        print(ob.lcs(s1, s2))
        print("~")

# } Driver Code Ends