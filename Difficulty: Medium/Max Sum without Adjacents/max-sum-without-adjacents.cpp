//{ Driver Code Starts
// Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
// User function template for C++
// User function template for C++
class Solution {
  public:
  // THE BELOW CODE IS USING DP:
    // int subsequence_sum(vector<int>&dp,vector<int>& arr,int ind)
    // {
    //     if(ind == 0)
    //     {
    //         return arr[ind];
    //     }
    //     if(ind < 0)
    //     {
    //         return 0;
    //     }
    //     if(dp[ind] != -1)
    //     {
    //         return dp[ind];
    //     }
    //     int pick = arr[ind] + subsequence_sum(dp,arr,ind-2);
    //     int non_pick = subsequence_sum(dp,arr,ind-1);
    //     return dp[ind] = max(pick,non_pick);
    // }
    // // calculate the maximum sum with out adjacent
    int findMaxSum(vector<int>& arr) {
        // code here
        // TABULATION METHOD
        int prev = arr[0];
        int prev2 = 0;
        for(int i=1;i<arr.size();i++)
        {
            int pick = arr[i] + prev2;
            int non_pick = prev;
            int current = max(pick,non_pick);
            prev2 = prev;
            prev = current;
            
        }
        return prev;
        
    }
};

//{ Driver Code Starts.

int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution obj;
        int res = obj.findMaxSum(arr);
        cout << res << endl;
        cout << "~" << endl;
        // string tl;
        // getline(cin, tl);
    }
    return 0;
}

// } Driver Code Ends