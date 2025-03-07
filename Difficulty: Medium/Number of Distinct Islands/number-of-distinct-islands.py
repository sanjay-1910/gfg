#User function Template for python3

import sys
from typing import List
sys.setrecursionlimit(10**8)

class Solution:
    
    def islands(self,grid,i,j,l,visited,baserow,basecol):
        visited[i][j] = True
        directions = [(i,j+1),(i+1,j),(i,j-1),(i-1,j)]
        for dir in directions:
            row = dir[0]
            col = dir[1]
            # l.append((baserow-row,basecol-col))
            if(row >=0 and col<len(grid[0]) and col>=0 and row< len(grid) and visited[row][col] == False and grid[row][col] == 1):
                l.append((baserow-row,basecol-col))
                self.islands(grid,row,col,l,visited,baserow,basecol)

                
    def countDistinctIslands(self, grid : List[List[int]]) -> int:        # code here
        s = set()
        visited = [[False]*len(grid[0]) for d in range(len(grid))]
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                if(visited[i][j] == False and grid[i][j] == 1):
                    l = []
                    baserow = i
                    basecol = j
                    self.islands(grid,i,j,l,visited,baserow,basecol)
                    t = tuple(l)
                    s.add(t)
        return len(s)
                    
                
  

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.countDistinctIslands(grid))
        print("~")
# } Driver Code Ends