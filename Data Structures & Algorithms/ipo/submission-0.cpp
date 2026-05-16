class Solution {
public:
    int findMaximizedCapital(int k, int w, vector<int>& profits, vector<int>& capital) {
        priority_queue<pair<int,int>,
        vector<pair<int,int>>,
        greater<pair<int,int>>> pq ; 
        for (int i=0;i<profits.size();++i){
            pq.push({capital[i],profits[i]});
        }
        priority_queue<pair<int,int>> prof;
        while(k>0 && (!prof.empty() || !pq.empty())){
          while(!pq.empty() && pq.top().first<=w){
            prof.push({pq.top().second,pq.top().first});
            pq.pop();
          }
          if (prof.empty()){
            break;
          }
          k--;
          w+=prof.top().first;
          prof.pop();
        }
        return w;
    }
};