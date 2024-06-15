# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,arr, n):
        if n==1:
            return 1
        left=[]
        right=[]
        l=r=0
        for i in range(0,n):
            l=l+arr[i]
            left.append(l)
            r=r+arr[n-i-1]
            right.append(r)
        right.reverse()
        for i in range(n):
            if i==0 and right[i+1]==0:
                return 1
            if i==n-1 and left[i-1]==0:
                return n
            if left[i]==right[i]:
                return i+1
        return -1
        # Your code here



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob = Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends