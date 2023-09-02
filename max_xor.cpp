// Your C++ code here
#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

// Trie node class
class TrieNode {
public:
    unordered_map<int, TrieNode*> children;
    int value;
};

// Insert a number into Trie
void insert(TrieNode* root, int num) {
    TrieNode* node = root;
    for (int i = 31; i >= 0; --i) {
        int bit = (num >> i) & 1;
        if (node->children.find(bit) == node->children.end()) {
            node->children[bit] = new TrieNode();
        }
        node = node->children[bit];
    }
    node->value = num;
}

// Find maximum XOR pair for a number
int findMaxXorPair(TrieNode* root, int num) {
    TrieNode* node = root;
    for (int i = 31; i >= 0; --i) {
        int bit = (num >> i) & 1;
        // Try to go the opposite bit direction to maximize XOR
        int oppBit = bit ^ 1;
        if (node->children.find(oppBit) != node->children.end()) {
            node = node->children[oppBit];
        } else {
            node = node->children[bit];
        }
    }
    return num ^ node->value;
}

// Find maximum XOR of any two elements in array
int findMaxXor(vector<int>& arr) {
    int max_xor = 0;
    TrieNode* root = new TrieNode();
    
    for (int num : arr) {
        // Insert into Trie
        insert(root, num);
        // Find maximum XOR for this number
        max_xor = max(max_xor, findMaxXorPair(root, num));
    }
    
    return max_xor;
}

// Test the program
int main() {
    vector<vector<int>> testCases = {
        {3, 10, 5, 25, 2, 8},
        {12, 15},
        {8, 1, 2, 12},
        {4, 6},
        {7, 8, 5},
        {0, 0, 0},
        {1, 1, 1},
        {8, 10, 2},
        {2, 4, 8},
        {2, 4, 8, 10}
    };
    
    for (int i = 0; i < testCases.size(); ++i) {
        cout << "Test case " << i + 1 << ": ";
        for (int num : testCases[i]) {
            cout << num << " ";
        }
        cout << endl;
        cout << "The maximum XOR of any two elements is: " << findMaxXor(testCases[i]) << endl;
        cout << "--------------------------------------------------" << endl;
    }
    
    return 0;
}
