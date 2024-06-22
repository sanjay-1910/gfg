class Solution:
    def ExtractNumber(self,sentence):
        #code here
        maxo=0
        l=list(sentence.split())
        for i in l:
            if i.isnumeric():
                if '9' not in i:
                    maxo=max(maxo,int(i))
        if maxo==0:
            return -1
        else:
            return maxo
    


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    S = input()
    ob = Solution()
    ans = ob.ExtractNumber(S)
    print(ans)

# } Driver Code Ends