#User function Template for python3


class Solution:
    def compareFrac (self, str):
        l=[]
        s=0
        a=""
        mid=0
        for i in range(0,len(str)):
            if str[i]=='/':
                s=int(a)
                a=""
            elif str[i]==',':
                l.append(s/int(a))
                a=""
                s=0
                mid=i
            elif i==len(str)-1:
                a=a+str[i]
                l.append(s/int(a))
            elif str[i]==" ":
                pass
            else:
                a+=str[i]
        if l[0]>l[1]:
            return str[0:mid]
        elif l[1]>l[0]:
            return str[mid+2:]
        else:
            return "equal"
                
            
            
                
            
            
        
        # code here
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends