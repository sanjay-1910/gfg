//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;
#define MAX_HEIGHT 100000

// Tree Node
class Node {
  public:
    int data;
    Node* left;
    Node* right;

    // Constructor to initialize a new node
    Node(int val) {
        data = val;
        left = NULL;
        right = NULL;
    }
};

// Utility function to create a new Tree Node
Node* newNode(int val) {
    return new Node(val);
}

// Function to Build Tree
Node* buildTree(string str) {
    // Corner Case
    if (str.length() == 0 || str[0] == 'N')
        return NULL;

    // Creating vector of strings from input
    // string after splitting by space
    vector<string> ip;

    istringstream iss(str);
    for (string str; iss >> str;)
        ip.push_back(str);

    // Create the root of the tree
    Node* root = newNode(stoi(ip[0]));

    // Push the root to the queue
    queue<Node*> queue;
    queue.push(root);

    // Starting from the second element
    int i = 1;
    while (!queue.empty() && i < ip.size()) {

        // Get and remove the front of the queue
        Node* currNode = queue.front();
        queue.pop();

        // Get the current node's value from the string
        string currVal = ip[i];

        // If the left child is not null
        if (currVal != "N") {

            // Create the left child for the current node
            currNode->left = newNode(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->left);
        }

        // For the right child
        i++;
        if (i >= ip.size())
            break;
        currVal = ip[i];

        // If the right child is not null
        if (currVal != "N") {

            // Create the right child for the current node
            currNode->right = newNode(stoi(currVal));

            // Push it to the queue
            queue.push(currNode->right);
        }
        i++;
    }

    return root;
}


// } Driver Code Ends
/*
// Tree Node
class Node {
  public:
    int data;
    Node* left;
    Node* right;

    // Constructor to initialize a new node
    Node(int val) {
        data = val;
        left = NULL;
        right = NULL;
    }
};
*/
class Solution {
public:
    void leftBoundary(Node *root, vector<int> &ans) {
        Node *cur = root->left;
        while (cur) {
            if (!(cur->left == NULL && cur->right == NULL)) // Exclude leaf nodes
                ans.push_back(cur->data);
            if (cur->left) cur = cur->left;
            else cur = cur->right;
        }
    }

    void rightBoundary(Node *root, vector<int> &ans) {
        vector<int> temp;
        Node *cur = root->right;
        while (cur) {
            if (!(cur->left == NULL && cur->right == NULL)) // Exclude leaf nodes
                temp.push_back(cur->data);
            if (cur->right) cur = cur->right;
            else cur = cur->left;
        }
        reverse(temp.begin(), temp.end()); // Reverse before inserting
        ans.insert(ans.end(), temp.begin(), temp.end());
    }

    void leafNodes(Node *root, vector<int> &ans) {
        if (root == NULL) return;
        if (root->left == NULL && root->right == NULL) {
            ans.push_back(root->data);
            return;
        }
        leafNodes(root->left, ans);
        leafNodes(root->right, ans);
    }

    vector<int> boundaryTraversal(Node *root) {
        vector<int> ans;
        if (root == NULL) return ans;
        if (root->left == NULL && root->right == NULL)
        {
            ans.push_back(root->data);
            return ans;
        }
        
        ans.push_back(root->data);

        // Left Boundary
        leftBoundary(root, ans);

        // Leaf Nodes
        leafNodes(root, ans);

        // Right Boundary
        rightBoundary(root, ans);

        return ans;
    }
};

//{ Driver Code Starts.

/* Driver program to test size function */
int main() {
    int t;
    string tc;
    getline(cin, tc);
    t = stoi(tc);
    while (t--) {
        string s, ch;
        getline(cin, s);
        Node* root = buildTree(s);
        Solution ob;
        vector<int> res = ob.boundaryTraversal(root);
        for (int i : res)
            cout << i << " ";
        cout << endl;

        cout << "~"
             << "\n";
    }
    return 0;
}

// } Driver Code Ends