#User function Template for python3
#User function Template for python3

class Solution:
    def findPermutation(self, s):
        answer = set()
        def per(string,start):
            if(start==len(string)):
                answer.add(''.join(string))
            for i in range(start,len(string)):
                string[start],string[i] = string[i],string[start]
                per(string,start+1)
                string[start],string[i] = string[i],string[start]       
        string = list(s)
        per(string,0)
        final = list(answer)
        return final
        # Code here
        

        


        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        S = input()
        ob = Solution()
        ans = ob.findPermutation(S)
        ans.sort()
        for i in ans:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends