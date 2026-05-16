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
        priority_queue<pair<int,int>,vector<pair<int,int>>,greater<pair<int,int>>> pq;
        for (auto i:followings[userId]){
            vector<pair<int,int>> tweetList = tweets[i];
            for (auto tweet:tweetList){
                pq.push(tweet);
                if (pq.size()>10){
                    pq.pop();
                }
            }
        }

            for (auto tweet:tweets[userId]){
                pq.push(tweet);
                if (pq.size()>10){
                    pq.pop();
                }
            }


        vector<int> ans ; 
        while(!pq.empty()){
            ans.push_back(pq.top().second);
            pq.pop();
        }
        reverse(ans.begin(),ans.end());
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
