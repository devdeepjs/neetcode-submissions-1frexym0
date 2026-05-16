class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        priority_queue<int> pq;
        for (auto i : stones){
            pq.push(i);
        }
        while((int)pq.size()>1){
            int x = pq.top();
            pq.pop();
            int y = pq.top();
            pq.pop();

            if (x==y){
                continue;
            }
            if (x<y){
                swap(x,y);
            }
            pq.push(x-y);
        }
        return (int)pq.size()>0 ? pq.top() : 0;
    }
};
