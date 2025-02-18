#{ 
 # Driver Code Starts
#Initial Template for Python 3
from typing import List


# } Driver Code Ends


import math
import heapq
class Solution:
    def distance(self,point):
        ans = math.sqrt((point[0]**2)+(point[1]**2))
        return ans
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        final = []
        min_heap = []
        heapq.heapify(min_heap)
        d = {}
        for i in points:
            result = self.distance(i)
            if(len(min_heap)<k):
                heapq.heappush(min_heap,-result)
                if result not in d:
                    d[result] = [i]
                else:
                    d[result].append(i)
            else:
                if(result<-min_heap[0]):
                    d[-min_heap[0]].pop(-1);
                    heapq.heapreplace(min_heap,-result)
                    if(result not in d.keys()):
                        d[result] = [i]
                    else:
                        d[result].append(i)
        c = 0
        for keys in d.keys():
            # if k-c >= len(d[keys]):
            #     final.extend(d[keys])
            #     c = c+len(d[keys])
            # else:
            #     final.extend(d[keys][ :k-c])
            final.extend(d[keys])
        return final
        
        
            
        
        
        
        # Your code here
        
        

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        t -= 1
        k = int(input())
        n = int(input())
        points = []
        for _ in range(n):
            x, y = map(int, input().split())
            points.append([x, y])
        
        solution = Solution()
        ans = solution.kClosest(points, k)
        ans.sort()
        for point in ans:
            print(point[0], point[1])
        print("~")

# } Driver Code Ends