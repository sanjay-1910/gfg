//{ Driver Code Starts
//Initial Template for C++


#include <bits/stdc++.h>
using namespace std;
#define MAX_HEIGHT 100000

// Tree Node
struct Node {
    int data;
    Node* left;
    Node* right;
};

// Utility function to create a new Tree Node
Node* newNode(int val) {
    Node* temp = new Node;
    temp->data = val;
    temp->left = NULL;
    temp->right = NULL;

    return temp;
}


// Function to Build Tree
Node* buildTree(string str) {
    // Corner Case
    if (str.length() == 0 || str[0] == 'N') return NULL;

    // Creating vector of strings from input
    // string after spliting by space
    vector<string> ip;

    istringstream iss(str);
    for (string str; iss >> str;) ip.push_back(str);

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
        if (i >= ip.size()) break;
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
//User function Template for C++

class Solution{
    public:
    void traverse(int sum,int &maxsum,Node* root)
    {
        if(root==NULL)
        {
            return;
        }
        if(root->left==NULL && root->right==NULL)
        {
         maxsum=max(maxsum,sum+root->data);
        }
        //sum=sum+root->data;
        traverse(sum+root->data,maxsum,root->left);
        traverse(sum+root->data,maxsum,root->right);
    }
    int maxPathSum(Node* root)
    {
        //code here
        int sum=0;
        int maxsum=INT_MIN;
        // if(root->left==NULL)
        // {
        //     sum=sum+root->data;
        //     traverse(sum,sum,root->right);
        //     return maxsum;
        // }
        // else if(root->right==NULL)
        // {
        //     sum=sum+root->data;
        //     traverse(sum,sum,root->left);
        //     return maxsum;
        // }
        // else
        // {
        // if(root==NULL)
        // {
        //     return 0;
        // }
        // if(root->left==NULL && root->right==NULL)
        // {
        //     return root->data;
        // }
        traverse(sum,maxsum,root);
        return maxsum;
    }
};

//{ Driver Code Starts.

/* Driver program to test size function*/

  

int main() {

   
    int t;
    scanf("%d ", &t);
    while (t--) {
        string s, ch;
        getline(cin, s);
        
        Node* root = buildTree(s);
        Solution ob;
        cout << ob.maxPathSum(root) << endl;
    }
    return 0;
}

// } Driver Code Ends