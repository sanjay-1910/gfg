class Solution:
    def find(self, parent, x):
        """Find the latest available slot (using path compression)."""
        if parent[x] == x:
            return x
        parent[x] = self.find(parent, parent[x])  # Path compression
        return parent[x]

    def JobSequencing(self, id, deadline, profit):
        jobs = []
        n = len(id)
        
        # Create list of jobs (id, deadline, profit)
        for i in range(n):
            jobs.append((id[i], deadline[i], profit[i]))

        # Sort jobs in decreasing order of profit
        jobs.sort(key=lambda x: x[2], reverse=True)

        # Find maximum deadline
        max_deadline = max(deadline)

        # Create a parent array for disjoint set (tracking available slots)
        parent = [i for i in range(max_deadline + 1)]

        count_jobs = 0
        total_profit = 0

        for job in jobs:
            job_id, job_deadline, job_profit = job

            # Find the latest available slot
            available_slot = self.find(parent, job_deadline)

            # If a free slot exists, assign the job
            if available_slot > 0:
                parent[available_slot] = self.find(parent, available_slot - 1)  # Union operation
                count_jobs += 1
                total_profit += job_profit

        return [count_jobs, total_profit]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        job_ids = list(map(int, input().split()))
        deadlines = list(map(int, input().split()))
        profits = list(map(int, input().split()))
        obj = Solution()
        ans = obj.JobSequencing(job_ids, deadlines, profits)
        print(ans[0], ans[1])
        print("~")

# } Driver Code Ends