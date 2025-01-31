#User function Template for python3

class Solution:
    def dfs(self,node,adj,visited,ans):
        visited[node] = 1
        for i in adj[node]:
            if(visited[i] == -1):
                ans.append(i)
                self.dfs(i,adj,visited,ans)
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        visited = [-1]*len(adj)
        ans = [0]
        self.dfs(0,adj,visited,ans)
        return ans
        # code here


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        # Create adjacency list with V vertices
        adj = [[] for i in range(V)
               ]  # List of lists (vector of vectors equivalent)

        # Reading edges
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        # Create an object of Solution class
        ob = Solution()
        ans = ob.dfsOfGraph(adj)

        # Printing the result
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
        print("~")
# } Driver Code Ends