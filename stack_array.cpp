#include <iostream>

class Stack
{
    private:
        int capacity;
        int sz = 0;
        int* arr;
    public:
        Stack(int capa = 10) {capacity = capa; arr = new int[capacity];}
        ~Stack(){};
        void push(int x)
        {
            if(sz < capacity)
            {
                *(arr+sz) = x;
                sz++;
            }
            else
                std::cout << "stack overflow!" << std::endl;
        }
        void pop()
        {
            if(sz == 0)
                std::cout << "stack underflow!" << std::endl;
            else
            {
                sz--;
            }
        }
        int top()
        {
            if(sz == 0)
            {
                std::cout << "stack is empty!" << std::endl;
                return -1;
            }
            else
                return *(arr+sz-1);
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
    Stack stack(3);
    stack.pop();
    stack.push(13);
    stack.push(99);
    stack.push(122);
    stack.push(11);
    std::cout << stack.top() << std::endl;
    stack.pop();
    std::cout << stack.top() << std::endl;
    stack.pop();
    stack.pop();
    std::cout << stack.top() << std::endl;
    std::cout << stack.size() << std::endl;

    
    return 0;
}