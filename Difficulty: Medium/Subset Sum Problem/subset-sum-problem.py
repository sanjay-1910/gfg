class Solution:
    def subset(self,arr,index,n,sumo,key,dp):
        if(sumo>key):
            return False
        if(sumo == key):
            return True
        if(index == n):
            return False
        # if(dp[index]!=-1):
        #     return dp[index]
        sumo = sumo + arr[index]
        if(self.subset(arr,index+1,n,sumo,key,dp)):
            return True
        sumo = sumo - arr[index]
        if(self.subset(arr,index+1,n,sumo,key,dp)):
            return True
        return False
    def isSubsetSum (self, arr, sum):
        dp = [-1]*len(arr)
        ans = self.subset(arr,0,len(arr),0,sum,dp)
        return ans
        
        # code here 
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends