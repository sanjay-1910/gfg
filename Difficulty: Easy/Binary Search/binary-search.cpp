//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++

class Solution {
  public:
    int binarysearch(vector<int> &arr, int k) {
        // code here
        int start_index=0;
        int end_index= arr.size()-1;
        int result =-1;

while(start_index<=end_index){
    
int middle = start_index + (end_index - start_index)/2;

        if( arr[middle]==k ){
            result = middle;
            end_index=middle-1;
        }
        
        else if(arr[middle]<k)
        {
            start_index = middle+1;
        }
        else{
            end_index = middle-1;
        }
}
                return result;

        
        
    } 
    
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int k;
        cin >> k;
        vector<int> arr;
        string input;
        cin.ignore();
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }
        Solution ob;
        int res = ob.binarysearch(arr, k);
        cout << res << endl;
        cout << "~" << endl;
    }
    return 0;
}

// } Driver Code Ends