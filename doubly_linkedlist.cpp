#include <iostream>
#include <climits>

struct Node
{
    int val;
    Node* prev = nullptr;
    Node* next = nullptr;
};

class DoublyLinkedList
{
    private:
        Node* head = nullptr;
        int sz = 0;
    public:
        DoublyLinkedList(){};
        ~DoublyLinkedList(){};
        void insert_val(int val)
        {
            Node* new_p = new Node;
            new_p->val = val;
            new_p->next = head;
            if(head != nullptr)
            {
                head->prev = new_p;
            }
            head = new_p;
            sz++;
        }
        void delete_val(int val)
        {
            Node* new_p = new Node;
            new_p->val = 0;
            new_p->next = head;
            Node* final_list = new_p;
            while(new_p->next != nullptr)
            {
                if(new_p->next->val == val)
                {
                    new_p->next = new_p->next->next;
                    //now new_p->next is actually old new_p->next->next
                    if(new_p->next != nullptr)
                        new_p->next->prev = new_p;
                    sz--;
                    break;
                }
                new_p = new_p -> next;
            }
            head = final_list->next;
        }
        void traversal()
        {
            Node* dummy = head;
            while(dummy != nullptr)
            {
                std::cout << dummy->val << std::endl;
                dummy = dummy->next;
            }
        }
        int top()
        {
            if(head != nullptr)
                return head->val;
            return INT_MAX;
        }
        int size()
        {
            return sz;
        }
};

int main()
{

    DoublyLinkedList dlist;
    dlist.delete_val(12);
    dlist.insert_val(3);
    dlist.insert_val(9);
    dlist.insert_val(45);
    std::cout << dlist.size() << std::endl;
    dlist.delete_val(3);
    std::cout << dlist.top() << std::endl;
    dlist.traversal();
    return 0;
}