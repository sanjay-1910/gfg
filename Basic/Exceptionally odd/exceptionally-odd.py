#User function Template for python3

class Solution:
    def getOddOccurrence(self, arr, n):
        # code here 
        c=arr[0]
        for i in range(1,n):
            c=c^arr[i]
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getOddOccurrence(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends