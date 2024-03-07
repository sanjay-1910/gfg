#User function Template for python3
class Solution:
    def getPairsCount(self, arr, n, k):
        d={}
        c=0
        for i in range(0,len(arr)):
            val=k-arr[i]
            if val in d.keys():
                c=c+d[val]
            if arr[i] not in d.keys():
                d[arr[i]]=1
            else:
                d[arr[i]]=d[arr[i]]+1
        return c
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getPairsCount(arr, n, k)
        print(ans)
        tc -= 1

# } Driver Code Ends