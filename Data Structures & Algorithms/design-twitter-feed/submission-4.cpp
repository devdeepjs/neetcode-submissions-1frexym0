class Twitter {
public:
    Twitter() {
        time = 0 ; 
    }
     
    int time ; 
    unordered_map<int,unordered_set<int>> followings; 
    unordered_map<int,vector<pair<int,int>>> tweets;
    
    void postTweet(int userId, int tweetId) {
        time++;
        tweets[userId].push_back({time,tweetId});
    }
    
    vector<int> getNewsFeed(int userId) {
        using State = tuple<int,int,int,int> ; 
        // time tweetId userId index 
        priority_queue<State> pq ; 
                    auto func = [&](int userId){
            int n = tweets[userId].size() ; 
            if (n>0){
                pq.push({tweets[userId][n-1].first,
                tweets[userId][n-1].second,
                userId,
                n-1});
            }
            };
        
        func(userId);
        for (auto i:followings[userId]){
            func(i);
        }

        vector<int> ans ; 
        while(!pq.empty() && ans.size()<10){
           State top = pq.top();
           int time = get<0>(top);
            int tweetId = get<1>(top);
             int userId = get<2>(top);
              int index = get<3>(top);
           pq.pop();
           ans.push_back(tweetId);
           if (index-1>=0){
              pq.push({tweets[userId][index-1].first,
              tweets[userId][index-1].second,
              userId,
              index-1});
           }
        }
        return ans;
    }
    
    void follow(int followerId, int followeeId) {
        if (followerId==followeeId){
            return;
        }
        followings[followerId].insert(followeeId);
    }
    
    void unfollow(int followerId, int followeeId) {
        followings[followerId].erase(followeeId);
    }
};
