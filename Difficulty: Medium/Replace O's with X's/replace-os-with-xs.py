#User function Template for python3

class Solution:
    def dfs(self,i,j,grid,new,visited):
        new[i][j] = 'O'
        visited[i][j] = True
        directions = [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]
        for dir in directions:
            row = dir[0]
            col = dir[1]
            if(row >=0 and col<len(grid[0]) and col>=0 and row< len(grid) and visited[row][col] == False and grid[row][col] == 'O'):
                # new[row][col] = 'O'
                self.dfs(row,col,grid,new,visited)
    def fill(self,  grid):
        visited = [[False]*len(grid[0]) for d in range(len(grid))]
        new =  [['X']*len(grid[0]) for d in range(len(grid))]
        for i in range(0,len(grid[0])):
            if(grid[0][i] == 'O' and not visited[0][i]):
                self.dfs(0,i,grid,new,visited)
            if(grid[len(grid)-1][i] == 'O' and not visited[len(grid)-1][i]):
                self.dfs(len(grid)-1,i,grid,new,visited)
        for j in range(0,len(grid)):
            if(grid[j][0] == 'O' and not visited[j][0]):
                self.dfs(j,0,grid,new,visited)
            if(grid[j][len(grid[0])-1] == 'O' and not visited[j][len(grid[0])-1]):
                self.dfs(j,len(grid[0])-1,grid,new,visited)
        return new
        
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            s = list(map(str, input().split()))
            mat.append(s)

        ob = Solution()
        ans = ob.fill(mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends