#User function Template for python3

class Solution:
	def MakeZeros(self, matrix):
	    ne=[r[:] for r in matrix]
		p=len(matrix[0])
		for i in range(0,len(matrix)):
		    for j in range(0,p):
		        if matrix[i][j]==0:
		            sumad=0
		            if i>0:
		                sumad=sumad+matrix[i-1][j]
		                ne[i-1][j]=0
		            if i<len(matrix)-1:
		                sumad=sumad+matrix[i+1][j]
		                ne[i+1][j]=0
		            if j>0:
		                sumad=sumad+matrix[i][j-1]
		                ne[i][j-1]=0
		            if j<p-1:
		                sumad=sumad+matrix[i][j+1]
		                ne[i][j+1]=0
		            ne[i][j]=sumad
	    for i in range(0,len(matrix)):
	        for j in range(0,p):
	            matrix[i][j]=ne[i][j]
		      
		            
		            
		            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n, m = input().split()
		n = int(n); m = int(m);
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int,input().split())))
		ob = Solution()
		ob.MakeZeros(matrix)
		for i in range(n):
			for j in range(m):
				print(matrix[i][j], end = " ")
			print()
# } Driver Code Ends