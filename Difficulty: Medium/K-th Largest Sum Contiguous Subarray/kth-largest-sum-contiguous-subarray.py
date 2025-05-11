from typing import List


class Solution:
    def kthLargest(self, arr, k) -> int:
        # code here
        min_heap = []
        n = len(arr)
    
        for i in range(n):
            sum_ = 0
            for j in range(i, n):
                sum_ += arr[j]
    
                if len(min_heap) < k:
                    heapq.heappush(min_heap, sum_)
                else:
                    if sum_ > min_heap[0]:
                        heapq.heappushpop(min_heap, sum_)
        return min_heap[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

# Position this line where user code will be pasted.

#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.kthLargest(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends