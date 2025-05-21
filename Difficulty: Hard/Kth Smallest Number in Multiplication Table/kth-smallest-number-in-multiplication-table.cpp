class Solution {
  public:
    int kthSmallest(int m, int n, int k) {
        // code here
        if(m>n){
            swap(m,n);
        }
        int ans = 0;
        int low = 1;
        int high = m*n;
        while(low<=high)
        {
            int mid = (low+high)/2;
            int count = 0;
            for(int i=1;i<=m;i++)
            {
                count += min(mid/i,n);
            }
            if(count < k)
            {
                low = mid+1;
            }
            else
            {
                high = mid-1;
                ans = mid;
            }           
        }
        return ans;
    }
};
