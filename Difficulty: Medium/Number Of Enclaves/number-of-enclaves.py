#User function Template for python3

from typing import List

class Solution: 
    def dfs(self,i,j,grid,new,visited):
        new[i][j] = 0
        visited[i][j] = True
        directions = [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]
        for dir in directions:
            row = dir[0]
            col = dir[1]
            if(row >=0 and col<len(grid[0]) and col>=0 and row< len(grid) and visited[row][col] == False and grid[row][col] == 1):
                self.dfs(row,col,grid,new,visited)
    def numberOfEnclaves(self, grid: List[List[int]]) -> int:
        # code here
        visited = [[False]*len(grid[0]) for d in range(len(grid))]
        # new =  [[]*len(grid[0]) for d in range(len(grid))]
        new = grid
        c = 0
        for i in range(0,len(grid[0])):
            if(grid[0][i] == 1 and not visited[0][i]):
                self.dfs(0,i,grid,new,visited)
            if(grid[len(grid)-1][i] == 1 and not visited[len(grid)-1][i]):
                self.dfs(len(grid)-1,i,grid,new,visited)
        for j in range(0,len(grid)):
            if(grid[j][0] == 1 and not visited[j][0]):
                self.dfs(j,0,grid,new,visited)
            if(grid[j][len(grid[0])-1] == 1 and not visited[j][len(grid[0])-1]):
                self.dfs(j,len(grid[0])-1,grid,new,visited)
        for k in range(0,len(new)):
            for l in range(0,len(new[0])):
                if(new[k][l] == 1):
                    c+=1
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int,input().strip().split())
        grid = []
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])

        obj=Solution()
        print(obj.numberOfEnclaves(grid))
        print("~")
# } Driver Code Ends