/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;
    Node() {
        val = 0;
        neighbors = vector<Node*>();
    }
    Node(int _val) {
        val = _val;
        neighbors = vector<Node*>();
    }
    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/

class Solution {
public:
    Node* dfs(Node* node,unordered_map<Node*,Node*> &vis){
         if (node==nullptr){
            return nullptr; 
         }
         if (vis.count(node)){
            return vis[node];
         }
         Node* newNode = new Node(node->val);
         vis[node] = newNode;
         for (auto i : node->neighbors){
            newNode->neighbors.push_back(dfs(i,vis));
         }
         return vis[node];
    }
    Node* cloneGraph(Node* node) {
        unordered_map<Node*,Node*> vis;
        return dfs(node,vis);
    }
};
