
class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        low = 0
        high = len(arr)-1
        floor = -1
        ceil  = -1
        arr.sort()
        while (low <= high):
            mid = (low+high)//2
            if (arr[mid] == x):
                # floor = arr[mid]
                # ceil = arr[mid]
                return [x,x]
            if arr[mid] < x:
                floor = arr[mid]
                low = mid+1
            else:
                ceil = arr[mid]
                high = mid - 1
        return [floor,ceil]
                
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])


if __name__ == "__main__":
    main()

# } Driver Code Ends