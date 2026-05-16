class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int k) {
        priority_queue<vector<int>> pq;
        for (auto i:points){
            pq.push({i[0]*i[0] + i[1]*i[1] , i[0],i[1]});
            if (pq.size()>k){
                pq.pop();
            }
        }
        vector<vector<int>> ans;
        while((int)pq.size()>0){
ans.push_back({pq.top()[1],pq.top()[2]});
pq.pop();
        }
        return ans;
    }
};
