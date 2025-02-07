#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    # prev = end[0]
    # c = 1
    def maximumMeetings(self,start,end):
        l=[]
        for j in range(0,len(start)):
            a = [start[j],end[j]]
            l.append(a)
        sorted_l = sorted(l,key=lambda x:(x[1]))
        # sorted_l = sorted(l, key=lambda x: (x[1]))
        prev = sorted_l[0][1]
        c = 1
        for i in sorted_l:
            sta,en = i[0],i[1]
            if(sta>prev):
                prev = en
                c+=1
        return c
            
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        start = list(map(int, input().strip().split()))
        end = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maximumMeetings(start, end))
        print("~")

# } Driver Code Ends