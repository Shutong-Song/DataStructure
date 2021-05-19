#include <iostream>
#include <string>
#include <climits>

struct Node
{
    std::string val;
    Node* prev;
    Node* next;
    Node(std::string value): val(value), prev(nullptr), next(nullptr) {};
};


class HashTable
{
    /*
    implemented using node array and handling collision using doubly-linked list
    support insert, delete, and search
    */
    private:
        int capacity = 13;
        Node** p;
        int hash_val(std::string str)
        {
            std::hash<std::string> hash_str;
            return hash_str(str)%capacity;
        }
    public:
        HashTable(int capa)
        {
            capacity = capa;
            p = new Node *[capacity];
            for(int i = 0; i < capacity; i++)
                p[i] = new Node("unknown");
        }
        ~HashTable(){}
        void insert_val(std::string astr)
        {
            /*

            */
            int str_idx = hash_val(astr);
            Node* new_node = new Node(astr);
            new_node->next = p[str_idx];
            p[str_idx]->prev = new_node;
            p[str_idx] = new_node;
        }
        void delete_val(std::string astr)
        {
            /*
            */
            int str_idx = hash_val(astr);
            Node* temp_node = search_val(astr);
            if(temp_node->val == "unknown")
            {
                std::cerr << "Key: " << astr << " not found!" << std::endl;
            }
            else
            {
                if(temp_node->prev != nullptr)
                    temp_node->prev->next = temp_node->next;
                if(temp_node->next != nullptr)
                    temp_node->next->prev = temp_node->prev;
            }
            

        }
        Node* search_val(std::string astr)
        {
            Node* dummy = new Node("unknown");
            int str_idx = hash_val(astr);
            Node* temp_node = p[str_idx];
            while(temp_node != nullptr)
            {
                if(temp_node->val == astr)
                    return temp_node;
                temp_node = temp_node->next;
            }
            return dummy;
        }



};


int main()
{
    HashTable new_hash = HashTable(3);
    std::string name1 = "James";
    std::string name2 = "Lily";
    std::string name3 = "Kevin";
    std::string name4 = "Allen";
    std::string name5 = "Barry";
    std::string name6 = "Bin";
    new_hash.insert_val(name1);
    new_hash.insert_val(name2);
    new_hash.insert_val(name3);
    new_hash.insert_val(name4);
    new_hash.insert_val(name5);
    new_hash.insert_val(name6);
    new_hash.delete_val("Kevin");
    new_hash.delete_val("Lily");
    new_hash.delete_val("James");
    new_hash.delete_val("Barry");
    new_hash.delete_val("Bin");
    new_hash.delete_val("Allen");

    
    return 0;
}