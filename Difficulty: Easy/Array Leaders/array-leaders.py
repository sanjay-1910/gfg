class Solution:
    def leaders(self, A):
        # Code here
        n = len(A)
        l=[]
        ans=[]
        max=A[-1]
        for i in range(len(A)-1,-1,-1):
            if(A[i]>max):
                max=A[i]
            l.append(max)
        l.reverse()
        for i in range(0,len(A)):
            if(A[i]>=l[i]):
                ans.append(A[i])
        return ans        #Code here
        
        # code here


#{ 
 # Driver Code Starts
t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().leaders(arr)  # find the leaders

    # Output formatting
    if s:
        print(" ".join(map(str, s)))  # Print leaders in the required order
    else:
        print("[]")  # Print empty list if no leaders are found

    print("~")

# } Driver Code Ends