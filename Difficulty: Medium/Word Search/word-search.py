class Solution:
    def bfs(self, mat, row, col, word, index, m, n, visited):
        if index == len(word) - 1:
            return True

        visited[row][col] = True  # Mark as visited
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # Up, Down, Left, Right

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < m and 0 <= new_col < n and not visited[new_row][new_col] and mat[new_row][new_col] == word[index + 1]:
                if self.bfs(mat, new_row, new_col, word, index + 1, m, n, visited):
                    return True

        visited[row][col] = False  # Backtrack
        return False

    def isWordExist(self, mat, word):
        m = len(mat)
        n = len(mat[0])
        visited = [[False for _ in range(n)] for _ in range(m)]  # Track visited cells

        for i in range(m):
            for j in range(n):
                if mat[i][j] == word[0]:  # Start DFS from matching first letter
                    if self.bfs(mat, i, j, word, 0, m, n, visited):
                        return True
        return False

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for tt in range(T):
        n = int(input())
        m = int(input())
        mat = []
        for i in range(n):
            a = list(input().strip().split())
            b = []
            for j in range(m):
                b.append(a[j][0])
            mat.append(b)
        word = input().strip()
        obj = Solution()
        ans = obj.isWordExist(mat, word)
        if ans:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends