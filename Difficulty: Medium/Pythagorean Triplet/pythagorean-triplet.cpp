class Solution {
  public:
    bool pythagoreanTriplet(vector<int>& arr) {
        // code here
        unordered_set<long long> squareSet;

    // Store squares of all elements
    for (int i = 0; i < arr.size(); i++) {
        squareSet.insert(1LL * arr[i] * arr[i]);
    }

    int n = arr.size();
    // Check all pairs for a^2 + b^2 = c^2
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            long long sum = 1LL * arr[i] * arr[i] + 1LL * arr[j] * arr[j];
            if (squareSet.find(sum) != squareSet.end()) {
                return true;
            }
        }
    }
    return false;
    }
};