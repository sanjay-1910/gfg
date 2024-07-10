#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) :
        maxo=0
        sumo=0
        d={}
        for i in range(0,len(arr)):
            sumo=sumo+arr[i]
            if sumo==k:
                maxo=max(maxo,i+1)
            elif sumo-k in d.keys():
                h=i-d[sumo-k]
                maxo=max(maxo,h)
            if sumo not in d.keys():
                d[sumo]=i
        return maxo



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends