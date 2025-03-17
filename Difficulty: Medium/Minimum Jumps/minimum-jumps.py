class Solution:
    def minJumps(self, arr):
        n = len(arr)
        if n == 1:
            return 0  # Already at the last index
        
        if arr[0] == 0:
            return -1  # Cannot move forward
        
        jumps = 1  # Initial jump
        maxReach = arr[0]  # The farthest index we can reach
        steps = arr[0]  # Steps we can still take in the current jump
        
        for i in range(1, n):
            if i == n - 1:
                return jumps  # If we reached the last index
            
            maxReach = max(maxReach, i + arr[i])  # Update max reachable index
            steps -= 1  # Use one step
            
            if steps == 0:  # If no more steps left
                jumps += 1  # Increment jump count
                
                if i >= maxReach:  # If we can't move further
                    return -1  
                
                steps = maxReach - i  # Reset steps based on the farthest reach
        
        return -1  # If not possible to reach the end


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)
        print("~")
# } Driver Code Ends