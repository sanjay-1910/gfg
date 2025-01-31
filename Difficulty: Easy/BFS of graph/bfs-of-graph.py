#User function Template for python3
class Solution:
    def bfs(self,node,adj,visited,queue,ans):
        visited[node] = 1
        queue.append(node)
        while queue:
            node = queue.pop(0)
            ans.append(node)
            for i in adj[node]:
                if visited[i] == -1:
                    queue.append(i)
                    visited[i] = 1
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: list[list[int]]) -> list[int]:
        visited = [-1]*len(adj)
        ans = []
        queue = []
        self.bfs(0,adj,visited,queue,ans)
        return ans# code here
        
        
    # class Solution:
    # def bfs(self,node,adj,visited,queue,ans):
    #     visited[node] = 1
    #     queue.append(node)
    #     while queue:
    #         node = queue.popleft()
    #         ans.append(node)
    #         for i in adj[node]:
    #             if visited[i] == -1:
    #                 queue.append(i)
    #                 visited[i] = 1
    # Function to return Breadth First Traversal of given graph.




#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for i in range(T):
        V = int(input())  # Number of vertices
        E = int(input())  # Number of edges
        adj = [[] for i in range(V)]  # Adjacency list
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)  # Undirected graph

        ob = Solution()
        ans = ob.bfsOfGraph(adj)
        print(" ".join(map(str, ans)))  # Print the BFS traversal result

# } Driver Code Ends