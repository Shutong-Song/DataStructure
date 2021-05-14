#include <iostream>
#include <climits>

struct Node
{
    int val;
    Node* next = nullptr;
};

class Singly
{
    private:
        Node* head = nullptr;
        int sz = 0;
    public:
        Singly(){};
        ~Singly(){};
        void insert_val(int val)
        {
            Node* new_p = new Node;
            new_p->val = val;
            new_p->next = head;
            head = new_p;
            sz++;
        }
        void delete_val(int val)
        {
            Node* dummy = new Node;
            dummy->val = 0;
            dummy->next = head;
            Node* final_list = dummy;
            while(dummy->next != nullptr)
            {
                if(dummy->next->val == val)
                {
                    dummy->next = dummy->next->next;
                    sz--;
                    break;
                }
                dummy = dummy->next;
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
    Singly list;
    list.delete_val(5);
    list.insert_val(3);
    list.insert_val(12);
    list.insert_val(7);
    std::cout << list.size() << std::endl;
    list.traversal();
    list.delete_val(3);
    list.traversal();
    std::cout << list.top() << std::endl;
    return 0;
}