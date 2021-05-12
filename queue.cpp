#include <iostream>

class Queue
{
    private:
        int* q = nullptr;
        int capacity = 10;
        int sz = 0;
        int head = -1;
        int tail = -1;
    public:
        Queue(int capa){capacity = capa; q = new int[capacity];};
        ~Queue(){};
        void enqueue(int val)
        {
            if(sz == 0)
            {
                head++;
                tail++;
                *(q+head) = val;
                sz++;
            }
            else if(sz == capacity)
            {
                std::cout << "Queue overflow!" << std::endl;
            }
            else if(tail == capacity - 1 && head != 0)
            {
                tail = 0;
                *(q+tail) = val;
                sz++;
            }
            else
            {
                tail++;
                *(q+tail) = val;
                sz++;
            }

        }
        void dequeue()
        {
            if(sz == 0)
            {
                std::cout << "Queue empty!" << std::endl;
            }
            else if(sz == 1)
            {
                head = -1;
                tail = -1;
                sz--;
            }
            else if(head == capacity - 1 && tail != 0)
            {
                head = 0;
                sz--;
            }
            else
            {
                head++;
                sz--;
            }
        }
        bool empty()
        {
            return sz==0?true:false;
        }
        int front()
        {
            if(head == -1)
                return -1;
            return *(q+head);
        }
        int back()
        {
            if(tail == -1)
                return -1;
            return *(q+tail);
        }
        int size()
        {
            return sz;
        }
};


int main()
{
    Queue q(3);
    q.dequeue();
    q.enqueue(12);
    q.enqueue(7);
    std::cout << q.front() << std::endl;
    std::cout << q.back() << std::endl;
    q.dequeue();
    std::cout << q.front() << std::endl;
    std::cout << q.back() << std::endl;
    q.enqueue(33);
    q.enqueue(41);
    q.enqueue(22);
    std::cout << q.front() << std::endl;
    std::cout << q.back() << std::endl;

    return 0;
}