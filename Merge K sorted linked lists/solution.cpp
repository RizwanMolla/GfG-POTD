#include <bits/stdc++.h>
using namespace std;

struct Node
{
    int data;
    Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }

};

struct Compare {
    bool operator()(Node* a, Node* b) {
        return a->data > b->data; 
    }
};

class Solution {
public:
    Node* mergeKLists(vector<Node*>& arr) {
        priority_queue<Node*, vector<Node*>, Compare> minHeap;

        for (Node* list : arr) {
            if (list) {
                minHeap.push(list);
            }
        }

        Node* dummy = new Node(0);
        Node* tail = dummy;

        while (!minHeap.empty()) {
            Node* minNode = minHeap.top();
            minHeap.pop();
            
            tail->next = minNode;
            tail = tail->next;
            
            if (minNode->next) {
                minHeap.push(minNode->next);
            }
        }

        return dummy->next;
    }
};