//{ Driver Code Starts
// C++ program to merge k sorted arrays of size n each
#include <bits/stdc++.h>
using namespace std;

// A Linked List node
struct Node {
    int data;
    Node* next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};

/* Function to print nodes in a given linked list */
void printList(Node* node) {
    while (node != NULL) {
        printf("%d ", node->data);
        node = node->next;
    }
    cout << endl;
}


// } Driver Code Ends
/*Linked list Node structure
 
struct Node
{
    int data;
    Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }

};
*/

class Solution {
public:
    struct Compare {
        bool operator()(Node* a, Node* b) {
            return a->data > b->data;  // Min-Heap based on node value
        }
    };

    Node* mergeKLists(vector<Node*>& lists) {
        priority_queue<Node*, vector<Node*>, Compare> minHeap;

        // Step 1: Insert the head of each linked list into the heap
        for (Node* list : lists) {
            if (list) minHeap.push(list);
        }

        // Step 2: Create a dummy node to help with merging
        Node* dummy = new Node(0);
        Node* tail = dummy;

        // Step 3: Extract minimum element and add next nodes
        while (!minHeap.empty()) {
            Node* minNode = minHeap.top();
            minHeap.pop();

            tail->next = minNode;
            tail = minNode;

            if (minNode->next) {
                minHeap.push(minNode->next);
            }
        }

        return dummy->next;  // The merged list starts from dummy->next
    }
};



//{ Driver Code Starts.

// Driver program to test the above functions
int main() {
    int t;
    cin >> t;
    cin.ignore();
    while (t--) {
        int n;
        cin >> n;
        cin.ignore();

        vector<Node*> v(n);

        for (int i = 0; i < n; i++) {
            string line;
            getline(cin, line);
            stringstream ss(line);

            Node* head = new Node(0);
            Node* temp = head;
            int x;
            while (ss >> x) {
                Node* newNode = new Node(x);
                temp->next = newNode;
                temp = temp->next;
            }
            v[i] = head->next;
        }

        Solution ob;
        Node* head = ob.mergeKLists(v);
        printList(head);
    }

    return 0;
}

// } Driver Code Ends