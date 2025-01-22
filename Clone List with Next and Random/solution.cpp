struct Node {
    int data;
    Node *next;
    Node *random;

    Node(int x) {
        data = x;
        next = 0;
        random = 0;
    }
};

class Solution {
  public:
    Node *cloneLinkedList(Node *head) {
        if (!head) return nullptr;

        Node* curr = head;
        while (curr) {
            Node* newNode = new Node(curr->data);
            newNode->next = curr->next;
            curr->next = newNode;
            curr = newNode->next;
        }

        curr = head;
        while (curr) {
            if (curr->random) {
                curr->next->random = curr->random->next;
            }
            curr = curr->next->next;
        }

        Node* dummy = new Node(0);
        Node* copy = dummy;
        curr = head;
        while (curr) {
            copy->next = curr->next;
            curr->next = curr->next->next;
            curr = curr->next;
            copy = copy->next;
        }

        return dummy->next;
    }
};