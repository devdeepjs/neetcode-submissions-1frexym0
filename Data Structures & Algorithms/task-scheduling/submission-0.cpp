class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        // A -> 1 
        // A -> 4
        // A -> 7 
        // B -> 2
        // C -> 3 
        queue<pair<int,int>> q ; 
        priority_queue<int> pq;
        unordered_map<int,int> mp ; 
        for (auto i:tasks){
            mp[i-'A']++;
        }
        for (auto &i:mp){
          pq.push(i.second);
        }
        // 3 ,1 ,1           
        // 1 , 1       2,2 
        int ans = 0;
        while(!pq.empty() || !q.empty()){
            while(!q.empty() && q.front().second<=ans){
                pq.push(q.front().first);
                q.pop();
            }
            if (!pq.empty()){
                int x = pq.top();
                pq.pop();
                x--;
                if (x>0){
                    q.push({x,ans+n+1});
                }
            }
            ans++;
        }
        return ans;
    }

};
