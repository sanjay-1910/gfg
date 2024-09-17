class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,x):
        #Your code here
        low = 0
        high = N - 1
        result = -1  # Initialize result to -1, which is the default if no floor is found
        
        while low <= high:
            mid = (low + high) // 2
            
            if A[mid] == x:
                return mid
            elif A[mid] < x:
                result = mid  # This is a potential floor, so update result
                low = mid + 1
            else:
                high = mid - 1
        
        return result

        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        NX = [int(x) for x in input().strip().split()]
        N = NX[0]
        X = NX[1]

        A = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.findFloor(A, N, X))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends