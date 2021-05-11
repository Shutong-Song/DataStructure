#include <iostream>

struct Node
{
    int val;
    Node* next;
};

class Stack
{
    private:
        Node* stack = nullptr;
        int sz = 0;
    public:
        void push(int x)
        {
            Node* temp = new Node();
            temp -> val = x;
            temp -> next = stack;
            stack = temp;
            sz++;
        }
        void pop()
        {
            if(sz == 0)
                std::cout << "stack underflow!" << std::endl;
            else
            {
                stack = stack->next;
                sz--;
            }
        }
        int top()
        {
            if(stack == nullptr) 
            {
                std::cout << "empty stack! return -1" << std::endl;
                return -1;
            }
            return stack->val;
        }
        bool empty()
        {
            return sz == 0?true:false;
        }
        int size()
        {
            return sz;
        }

};

int main()
{
    Stack obj_stack;
    obj_stack.pop();
    obj_stack.push(3);
    obj_stack.push(12);
    std::cout << obj_stack.top() << std::endl;
    obj_stack.pop();
    std::cout << obj_stack.top() << std::endl;
    std::cout << obj_stack.size() << std::endl;
    obj_stack.pop();
    obj_stack.pop();
    std::cout << obj_stack.size() << std::endl;
    std::cout << obj_stack.top() << std::endl;
    return 0;
}