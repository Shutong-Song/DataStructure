#include <iostream>
#include <vector>
#include <algorithm>

//build tree node
struct Node
{
    int val;
    Node* left;
    Node* right;
    Node(int _v) : val(_v), left(nullptr), right(nullptr) {};
};



class BTree
{
    /*
    1. construct a root pointer point to the root of a tree
    2. Three binary tree traversal has been developed using iterative methods: inorder, preorder, and postorder
    3. all iterative methods are using stack data structure
    */
    private:
        Node* root = nullptr;
    public:
        BTree(Node* rnode){root = rnode;} //class constructor to assign a binary tree to root pointer
        ~BTree(){} //destructor
        std::vector<int> inorder_iter(std::vector<int> &res)
        {
            Node* dummy = root;
            std::vector<Node*> astack;
            while(true)
            {
                while(dummy != nullptr)
                {
                    astack.push_back(dummy);
                    dummy = dummy->left;
                }
                if(astack.empty())
                    break;
                Node* temp_node = astack.back();
                astack.pop_back();
                res.push_back(temp_node->val);
                dummy = temp_node->right;
            }
            return res;
        }
        std::vector<int> preorder_iter(std::vector<int> &res)
        {
            Node* dummy = root;
            if(dummy != nullptr)
            {
                std::vector<Node*> stack;
                stack.push_back(dummy);
                while(!stack.empty())
                {
                    Node* temp_node = stack.back();
                    stack.pop_back();
                    res.push_back(temp_node->val);
                    if(temp_node->right != nullptr) 
                        stack.push_back(temp_node->right);
                    if(temp_node->left != nullptr)
                        stack.push_back(temp_node->left);
                }
            }
            return res;
        }
        std::vector<int> postorder_iter(std::vector<int> &res)
        {
            Node* dummy = root;
            if(dummy != nullptr)
            {
                std::vector<Node*> stack;
                stack.push_back(dummy);
                while(!stack.empty())
                {
                    Node* temp_node = stack.back();
                    stack.pop_back();
                    res.push_back(temp_node->val);
                    if(temp_node->left != nullptr)
                        stack.push_back(temp_node->left);
                    if(temp_node->right != nullptr)
                        stack.push_back(temp_node->right);
                }
                std::reverse(res.begin(), res.end());
            }
            return res;
        }
        
};


int main()
{
    Node* n1 = new Node(12);
    Node* n2 = new Node(33);
    Node* n3 = new Node(71);
    Node* n4 = new Node(6);
    Node* n5 = new Node(59);
    Node* n6 = new Node(17);
    Node* n7 = new Node(11);
    n1->left = n2;
    n1->right = n3;
    n2->right = n4;
    n4->left = n5;
    n3->left = n6;
    n3->right = n7;
    BTree root(n1);
    std::vector<int> res;
    root.inorder_iter(res);
    for(auto val: res)
        std::cout << val << std::endl;
    std::vector<int> res1;
    root.preorder_iter(res1);
    for(auto val1: res1)
        std::cout << val1 << std::endl;
    std::vector<int> res2;
    root.postorder_iter(res2);
    for(auto val2: res2)
        std::cout << val2 << std::endl;
    return 0;
}